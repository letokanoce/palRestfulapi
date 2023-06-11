from typing import Union, List, Any

from fastapi import APIRouter, Depends, Query
from neo4j import Session

from app.handler.manager import Neo4jContextManager
from app.instance import neo4j_driver
from app.utils.formatter import convert_list_to_dict

router = APIRouter()


@router.get('/neo4j/nodes', response_description="Get nodes")
def get_nodes(labels: Union[List[str], None] = Query(default=None),
              properties: Union[List[Any], None] = Query(default=None),
              session: Session = Depends(neo4j_driver.create_session)):
    with Neo4jContextManager(session=session) as neo4j_ctxt_mgr:
        props = convert_list_to_dict(properties)
        try:
            result = neo4j_ctxt_mgr.query_node(labels=labels, properties=props)
            return result
        except Exception as e:
            raise Exception(f"Error occurred while getting nodes: {e}")

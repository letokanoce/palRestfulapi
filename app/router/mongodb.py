from typing import Union, List

from fastapi import APIRouter, Depends, Query
from pymongo.client_session import ClientSession

from app.handler.manager import MongodbContextManager
from app.instance import mongodb_client

router = APIRouter()


@router.get('/mongodb/basic', response_description="Get specific documents")
def get_nodes(keywords: Union[List[str], None] = Query(default=None),
              session: ClientSession = Depends(mongodb_client.create_session)):
    with MongodbContextManager(session=session, database_name="image",
                               collection_name="collage") as mongodb_ctxt_mgr:
        try:
            query_filter = {"label": {"$all": keywords or []}}
            projection = {"_id": False, "name": True, "label": True, "strength": True}
            result = mongodb_ctxt_mgr.query(filter=query_filter, projection=projection)
            return result
        except Exception as e:
            raise Exception(f"Error occurred while getting documents: {e}")

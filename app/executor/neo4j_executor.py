from typing import List

from app.handler.neo4j_handler import Neo4jHandler


class Neo4jQuerier:
    def __init__(self, handler: Neo4jHandler):
        self.handler = handler

    def query_node(self, nodes_id: List[str]):
        try:
            result = [self.handler.query_node_by_id(node_id=node_id) for node_id in nodes_id]
            print(f"Query executed successfully, found {len(result)} nodes")
            return result
        except Exception as e:
            raise Exception(f"Error occurred while finding nodes: {e}")

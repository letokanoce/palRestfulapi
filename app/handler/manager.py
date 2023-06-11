from neo4j import Session
from pymongo.client_session import ClientSession

from app.handler.neo4j_handler import Neo4jHandler
from app.handler.mogodb_handler import MongodbHandler


class Neo4jContextManager:
    def __init__(self, session: Session):
        self.session = session

    def __enter__(self):
        self.transaction = self.session.begin_transaction()
        return Neo4jHandler(self.transaction)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            try:
                self.transaction.commit()
            except Exception as e:
                self.transaction.rollback()
                raise ConnectionError(f"Error occurred while committing Neo4j transaction: {e}")
        else:
            self.transaction.rollback()
        self.session.close()


class MongodbContextManager:
    def __init__(self, session: ClientSession, database_name: str, collection_name: str):
        self.session = session
        self.database_name = database_name
        self.collection_name = collection_name

    def __enter__(self):
        self.session.start_transaction()
        return MongodbHandler(self.session, self.database_name, self.collection_name)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            try:
                self.session.commit_transaction()
            except Exception as e:
                self.session.abort_transaction()
                raise ConnectionError(f"Error occurred while committing MongoDB transaction: {e}")
        else:
            self.session.abort_transaction()
        self.session.end_session()

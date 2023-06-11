from pymongo.client_session import ClientSession
from pymongo.errors import PyMongoError


class MongodbHandler:
    def __init__(self, session: ClientSession, database_name: str, collection_name: str):
        self.session = session
        self.database_name = database_name
        self.collection_name = collection_name
        self.collection = self.get_collection()

    def get_collection(self):
        db = self.session.client.get_database(self.database_name)
        return db.get_collection(self.collection_name)

    def query(self, *args, **kwargs):
        try:
            query_result = self.collection.find(*args, **kwargs, session=self.session)
            result = list(query_result)
            print(f"Query executed successfully, found {len(result)} records")
            return result
        except Exception as e:
            raise PyMongoError(f"Error occurred while querying: {e}")

    def insert(self, *args, **kwargs):
        try:
            result = self.collection.insert_many(*args, **kwargs, session=self.session)
            print(f"{len(result.inserted_ids)} document(s) inserted successfully")
            return result.inserted_ids
        except Exception as e:
            raise PyMongoError(f"Error occurred while inserting documents: {e}")

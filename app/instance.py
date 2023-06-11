from app.configuration.configs import *
from app.db.cache_driver import RedisDriver
from app.db.connector import Neo4jDriver, MongodbDriver

neo4j_settings = Neo4jSettings()
mongodb_settings = MongodbSettings()
redis_settings = RedisSettings()

neo4j_driver = Neo4jDriver(settings=neo4j_settings, max_pool_size=10)
mongodb_client = MongodbDriver(settings=mongodb_settings)
redis_client = RedisDriver(redis_settings)

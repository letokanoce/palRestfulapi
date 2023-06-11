from app.db.cache_driver import RedisDriver


class RedisHandler:
    # Initialize RedisHandler
    def __init__(self, cache_driver: RedisDriver):
        self.client = cache_driver.client

    # Get value associated with a key
    def get_from_redis(self, key: str):
        try:
            # Get value from redis
            query_value = self.client.hgetall(key)

            # Check if key exists in the cache
            if not query_value:
                print(f"Key '{key}' not found.")
                return None

            # Decode bytes to string
            result = {k.decode('utf8'): v.decode('utf8') for k, v in query_value.items()}
            print(f"Found value for key '{key}': {result}")
            return result
        except Exception as e:
            print(f"Error occurred while finding the value for key '{key}': {e}")

    # Set key-value pair in the cache
    def set_to_redis(self, key: str, value: dict):
        try:
            # Set key-value pair in redis
            self.client.hmset(key, value)
            print(f"Set value '{value}' for key '{key}'.")
        except Exception as e:
            print(f"Error occurred while setting the value for key '{key}': {e}")

    # Clear all key-value pairs in the cache
    def clear(self):
        try:
            self.client.flushall()
            print("All keys and values have been cleared from the cache.")
        except Exception as e:
            print(f"Error occurred while clearing the cache: {e}")

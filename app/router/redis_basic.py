from fastapi import APIRouter

from app.handler.cache_handler import RedisHandler
from app.instance import redis_client

router = APIRouter()


@router.delete("/redis/flush")
async def set_to_redis():
    redis_handler = RedisHandler(redis_client)
    redis_handler.clear()

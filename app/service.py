from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.router.mongodb import router as mongodb_router
from app.router.neo4j_advanced import router as neo4j_router_advanced
from app.router.neo4j_basic import router as neo4j_router_basic
from app.router.redis_basic import router as redis_router

app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_credentials=True,
                   allow_origins=["*"],
                   allow_methods=["*"],
                   allow_headers=["*"])


@app.get("/")
async def read_root():
    return {"HELLO": "Pal Data Manipulation"}


app.include_router(neo4j_router_basic)
app.include_router(neo4j_router_advanced)
app.include_router(mongodb_router)
app.include_router(redis_router)

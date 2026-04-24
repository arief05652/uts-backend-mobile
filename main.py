from contextlib import asynccontextmanager

from fastapi import FastAPI
from tortoise import Tortoise

from database import TORTOISE_ORM
from src.routes import link_route, protect_direct, user_route


@asynccontextmanager
async def lifespan(app: FastAPI):
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()
    yield
    await Tortoise.close_connections()


app = FastAPI(lifespan=lifespan)


app.include_router(user_route, prefix="/user")
app.include_router(link_route, prefix="/link")
app.include_router(protect_direct)

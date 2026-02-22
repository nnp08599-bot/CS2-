from contextlib import asynccontextmanager

from fastapi import FastAPI
from pydantic import BaseModel

from db import init_db, list_demos


class DemoOut(BaseModel):
    id: int
    filename: str
    date_added: str


@asynccontextmanager
async def lifespan(_: FastAPI):
    init_db()
    yield


app = FastAPI(title="CS2 Demo Analytics MVP", lifespan=lifespan)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/demos", response_model=list[DemoOut])
def get_demos() -> list[DemoOut]:
    return [DemoOut(**row) for row in list_demos()]

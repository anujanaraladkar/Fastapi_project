from typing import Optional

from pydantic import BaseModel

from fastapi import FastAPI


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user is added"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.post("/items/")
async def create_item(item: Item):
    return item


@app.get("/users/hi")
async def demo():
    return {"hello-anuja"}


@app.get("/users/")
async def ab():
    return {"how r you"}

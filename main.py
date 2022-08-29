from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


'''
import sentry_sdk
from sentry_sdk import set_tag
from sentry_sdk.integrations.starlette import StarletteIntegration
from sentry_sdk.integrations.fastapi import FastApiIntegration'''


'''
sentry_sdk.init(
    dsn="https://b158dd0adee348848aa4252a33ac954a@o1351339.ingest.sentry.io/6631845",
    environment="qa",
    integrations=[
        StarletteIntegration(),
        FastApiIntegration(),
    ],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=1.0,
)

app = FastAPI()

set_tag("page.locale", "de-at")

@app.get("/sentry-debug")
async def trigger_error():
    division_by_zero = 1/0'''


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.post("/items/")
async def
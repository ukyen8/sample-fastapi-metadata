from fastapi import FastAPI
from src.models import MetadataTag, ExternalDocs

user_tag = MetadataTag(
    name="user",
    description="Endpoints related to user data.",
)
order_tag = MetadataTag(
    name="order",
    description="Endpoints related to order data.",
    external_docs=ExternalDocs(
        description="External order documentation.", url="https://example.com"
    ),
)
store_tag = MetadataTag(
    name="store", description="Endpoints related to store data."
)

metadata_tags = [user_tag, order_tag, store_tag]
app = FastAPI(openapi_tags=[tag.dict(by_alias=True) for tag in metadata_tags])


@app.get("/user", tags=[user_tag.name])
async def get_user():
    return {"name": "bob"}


@app.get("/users", tags=[user_tag.name])
async def get_users():
    return [{"name": "bob"}, {"name": "james"}]


@app.get("/order", tags=[order_tag.name])
async def get_order():
    return {"order": {"id": 123, "total": 500}}


@app.get("/store", tags=[store_tag.name])
async def get_store():
    return {"name": "MyStoreName"}

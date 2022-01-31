from curses import noecho
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None  # Optional


app = FastAPI()

# POST is for creating a new item


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})

    return item_dict

# In order to test POST, go to localhost:8000/docs and Try it out, Execute :)

# PUT can be used for update operations


@app.put("/items/{item_id}")
async def create_itemm(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}


# PUT with query
@app.put("/item/{item_id}")
async def create_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if item.tax:
        price_with_tax = item.price + item.tax
        result.update({"price_with_tax": price_with_tax})
    if q:
        result.update({"q": q})
    return result

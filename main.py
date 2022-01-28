from lib2to3.pgen2.token import OP
from typing import Optional

from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):       # Without none it would be required, you may declare a type
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.price, "item_id": item_id}

# POST: to create data.
# GET: to read data.
# PUT: to update data.
# DELETE: to delete data.

# Path operations are evaluated in order, you need to make sure that the path for /users/me is declared before the one for /users/{user_id}

@app.get("/users/me")
async def read_user_me(user_id: str):
    return {"user_id": "current user"}

@app.get("users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

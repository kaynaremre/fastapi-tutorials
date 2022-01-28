from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {
    "item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]

# http://127.0.0.1:8000/items/?skip=0&limit=10 -- eg .[1:2]


@app.get("/items/{item_id}")                # Default None id, q
async def read_item2(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:      # If q is entered
        item.update({"q": q})
    if not short:
        item.update({"BOOOL": "BOOOOOOOLLLLL"})
    return item           # If q is not entered

# http://127.0.0.1:8000/items/Foo?short=False
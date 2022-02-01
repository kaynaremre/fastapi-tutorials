from fastapi import FastAPI, Query

app = FastAPI()


# Queries can be limited
@app.get("/items/")
async def read_items(q: str | None = Query(None, min_length=2, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# when you need to declare a value as required while using Query, you can use ... as the first argument:
@app.get("/items/ha")
async def read_items(q: str | None = Query(..., min_length=2, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# By declaring a list for queries, multiple query parameters can be entered
@app.get("/items/multi")
async def read_items(q: list[str] | None = Query(None)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

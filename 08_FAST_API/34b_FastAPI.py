from fastapi import FastAPI

app = FastAPI()

# Define a route with path and query parameters
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

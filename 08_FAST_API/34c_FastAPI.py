from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In-memory storage for items
items = []

# Pydantic model for an item
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool

# POST route to add an item
@app.post("/items/")
def create_item(item: Item):
    items.append(item.dict())  # Add item to the list
    return {"message": "Item successfully added"}

# GET route to retrieve all items
@app.get("/items/")
def get_items():
    return {"items": items}
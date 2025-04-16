from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float

items_db: Dict[int, Item] = {}

@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    items_db[item_id] = item
    return {"message": "Item created", "item": item}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return items_db.get(item_id, {"error": "Item not found"})

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    items_db[item_id] = item
    return {"message": "Item updated", "item": item}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id in items_db:
        del items_db[item_id]
        return {"message": "Item deleted"}
    return {"error": "Item not found"}

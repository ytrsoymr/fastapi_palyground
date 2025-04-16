from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    return Item(name="Sample Item", price=19.99)

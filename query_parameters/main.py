from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")
def read_item(item_id: int, name: str = None):
    return {"item_id": item_id, "name": name}

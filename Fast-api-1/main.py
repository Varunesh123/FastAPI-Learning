from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name : str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"Hello" : "Varun"}

@app.get("/items/{items_id}")
def read_item(items_id: int, q: Union[str, None] = None):
    return {"item_id": items_id, "q": q}

@app.put("/items/{items_id}")
def update_item(items_id: int, item: Item):
    return {"Item_name": item.name, "items_id": items_id}
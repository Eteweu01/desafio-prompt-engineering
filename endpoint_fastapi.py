from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import date
from uuid import uuid4

app = FastAPI()

class Item(BaseModel):
    nome: str = Field(..., max_length=25)
    valor: float
    data: date

@app.post("/item")
def criar_item(item: Item):
    if item.data > date.today():
        raise HTTPException(status_code=400, detail="A data não pode ser superior à data atual.")
    
    item_dict = item.dict()
    item_dict["uuid"] = str(uuid4())
    return item_dict

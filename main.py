from  fastapi import FastAPI

from pydantic import BaseModel
from datetime import datetime
from typing import Union
from enum import Enum


class ModelName(str,Enum):
    alexnet= 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'


class Item(BaseModel):
    name:str
    description : Union[str,None] = None
    price : float
    tax : Union[float,None] = None



db = [{"item_name":"foo"},{"item_name":"anicet"},{"item_name":"jojo"}]


app = FastAPI()


@app.post("/items_/")
async def create_item(item:Item):
    item_dict = item.dict()
    if item_dict.tax :
        prices_with_tax = item_dict.price +item_dict.tax
        item_dict.update({"price_with_tax" : prices_with_tax})
    return item

@app.get('/')
async def root():
    return {'message':'Hello world'}


@app.get("/files/{file_path:path}")
async def read_file(file_path:str):
    return f"file is :{file_path}"


@app.get("/items/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: Union[int, None] = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item

@app.get("/users")
async def read_users():
    return ["kacou","Lois"]

@app.get("/items_name/{skip}")
async def read_items(skip:int,limite:int=10):
    return db[skip,skip+limite]

@app.get('/models/{model_name}')
async def get_model(model_name:ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name" : model_name,"message":"Deep Learning FTW"}
    if model_name.value == 'lenet':
        return {"model_name":model_name,"message":"LeCNN all the images"}
    return {"model_name" : model_name,"message":"Have some residuals"}

from  fastapi import FastAPI

from pydantic import BaseModel
from datetime import datetime
from typing import Union
from enum import Enum


class ModelName(str,Enum):
    alexnet= 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'


db = [{"item_name":"foo"},{"item_name":"anicet"},{"item_name":"jojo"}]


app = FastAPI()




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
# @app.get("/items/{item_id}")
# async def read_item(item_id:str,q:Union[str,None] = None,short:bool = False):
#     item = {"item" : item_id}
#     if q:
#         item.update({"q":q})
#     if not short:
#         item.update({"description":"this is a amazing item but have a long description"})
#     return {'item_id':item}

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

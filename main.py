from  fastapi import FastAPI

from pydantic import BaseModel
from datetime import datetime

from enum import Enum


class ModelName(str,Enum):
    alexnet: 'alexnet'
    resnet : 'resnet'
    lenet : 'lenet'




app = FastAPI()




@app.get('/')
async def root():
    return {'message':'Hello world'}

@app.get("/items/{item_id}")
async def read_item(item_id:int):
    return {'item_id':item_id}

@app.get("/users")
async def read_users():
    return ["kacou","Lois"]

@app.get('/models/{model_name}')
async def get_model(model_name:ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name" : model_name,"message":"Deep Learning FTW"}
    if model_name.value == 'lenet':
        return {"model_name":model_name,"message":"LeCNN all the images"}
    return {"model_name" : model_name,"message":"Have some residuals"}

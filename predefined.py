from email import message
from enum import Enum
import re

from fastapi import FastAPI

class ModelName(str, Enum):
    porsche = "porsche"
    bmw = "bmw"
    audi = "audi"

app2 = FastAPI()

@app2.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.porsche:
        return {"model_name" : model_name, "message" : "Cayenne"}
    
    if model_name == ModelName.bmw:
        return {"model_name" : model_name, "message" : "730Li"}
    
    if model_name == ModelName.audi:
        return {"model_name" : model_name, "message" : "RS8"}


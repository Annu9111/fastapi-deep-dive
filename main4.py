from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Users(BaseModel):
    name:str
    age:int

#post request
# @app.post("/create_user")
# def new_user(name:str=None,age:int=3):
#     return {"Name":name , "Age":age}


@app.post("/create_user")
def new_user(user:Users):
    return {
        "message":"user created",
        "data":user        
    }


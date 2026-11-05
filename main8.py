from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name:str
    age:int
    password:int

class userResponse(BaseModel):
    name:str
    age:int

@app.get("/user",response_model=userResponse)
def get_user():
    return {
        "name":"mohit",
        "age":23,
        "password":"12344"
    }
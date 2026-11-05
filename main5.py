from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name:str
    age:int
    email:str

@app.post("/create_user")
def create_user(user:User):
    return {
        "message":"user created",
        "data":user
    }
    
#nested models

class Address(BaseModel):
    city:str
    pincode:int
    
class person(BaseModel):
    name:str
    age:int
    address:Address
    
@app.post("/person")
def create_person(per:person):
    return {
        "message":"person created !",
        "data":per
    }
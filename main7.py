from fastapi import FastAPI
from pydantic import BaseModel

app  = FastAPI()

user_list = []

class User(BaseModel):
    name:str
    age:int 
    
@app.post("/users")
def create_users(user:User):
    user_list.append(user)
    return {"message":"user created successfully",
            "data":user}
    
@app.put("/users/{user_id}")
def updated_user(user_id:int,user:User,notify:bool=False):
    if 0<=user_id < len(user):
        user_list[user_id]=user
        
        return {"message":"user updated"}
    
    return {"error":"user not found"}




 
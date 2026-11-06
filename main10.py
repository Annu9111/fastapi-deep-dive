from fastapi import FastAPI,HTTPException,Request
from fastapi.responses import JSONResponse

app= FastAPI()

@app.get("/user/{user_id}")
def get_user(user_id:int):
    if user_id!=1:
        raise HTTPException(status_code=404,detail="user not found")
    return {
         "id":1,
         "name":"mohit"
    }


class userNotFoundException(Exception):
    def __init__(self,name:str):
        self.name=name

@app.exception_handler(userNotFoundException)
def user_not_found(request:Request,exc :userNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "status":"error",
            "message":f"user {exc.name} not found"
        }
    )
    

@app.get("/user/{name}")
def get_user(name:str):
    if name != "mohit":
        raise userNotFoundException(name)
    
    return {
        "name":name
    }
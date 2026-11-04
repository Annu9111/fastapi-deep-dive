from fastapi import FastAPI

app = FastAPI()

@app.post("/create_user")
def new_user(name:int,age:str):
    return {"Name":name , "Age":age}


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos=[]

class Todos(BaseModel):
    id:int
    title:str
    isCompleted:bool

@app.post("/create_todos")
def create_todos(task:Todos):
    todos.append(task)
    return {
        "message":"todo id created successfully!!"
    }
    



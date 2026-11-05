from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos=[]

class Todos(BaseModel):
    id:int
    title:str
    isCompleted:bool

@app.post("/todos")
def create_todos(task:Todos):
    todos.append(task)
    return {
        "message":"todo id created successfully!!"
    }
    
 
@app.get("/todos")
def get_data():
    return todos


@app.get("/todos/{todo_id}")
def get_item(todo_id:int):
    for todo in todos:
        if todo.id == todo_id :
            return todo
    return {"error":"todo not found"}


@app.put("/todos/{todo_id}")
def update_data(todo_id:int,updated_todo:Todos):
    for index,todo in enumerate(todos):
        if todo.id==todo_id:
            todos[index]=updated_todo
            return {"message":"todo is updated successfully"}
    return {"error":"id deos not found"}


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int):
    for index,todo in todos:
        if todo.id==todo_id:
            todos.pop(index)
            return {
                "message":"todo is deleted successfully"
            }
    return {
        "error":"id not found"
    }


    


from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()

class Todo(BaseModel):
    id:int
    name:str
    discription:str

todos = []
    

@app.get("/")
def home():
    return todos

@app.post("/")
def create_todo(todo:Todo):
    todos.append(todo)
    return{
        "message":"todo successfully created"
    }

@app.put("/{todo_id}")
def update(todo_id:int,new_todo:Todo):
    for index,todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = new_todo
            return {
                "message":"todo updated successfully"
            }
        else:
            raise HTTPException(status_code=404, detail="id not found")

@app.delete("/{todo_id}")
def delete(todo_id:int):
    for index,todo in enumerate(todos):
        if todo.id == todo_id:
            del todos[index]
            return{
                "message":"todo deleted successfully"
            }
        else:
            raise HTTPException(status_code=404,detail="todo not found")
        
            
 




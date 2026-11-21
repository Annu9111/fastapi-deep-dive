from fastapi import HTTPException,APIRouter,Depends
from pydantic import BaseModel
from database import get_db
from sqlalchemy.orm import Session
from models import Todo
from typing import List

router = APIRouter()

class TodoCreate(BaseModel):
    id:int
    name:str
    discription:str
    done:bool

class todo_response(TodoCreate):
    id:int

todos = []
    

@router.get("/")
def home():
    return todos

@router.post("/",response_model=todo_response) 
def create_todo(todo:TodoCreate,db:Session=Depends(get_db)):
    new_todo = Todo(title=todo.title,description=todo.description,done=todo.done)
    db.add(new_todo)
    db.commit()
    
    return new_todo

@router.put("/{todo_id}")
def update(todo_id:int,new_todo:TodoCreate):
    for index,todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = new_todo
            return {
                "message":"todo updated successfully"
            }
        else:
            raise HTTPException(status_code=404, detail="id not found")

@router.delete("/{todo_id}")
def delete(todo_id:int):
    for index,todo in enumerate(todos):
        if todo.id == todo_id:
            del todos[index]
            return{
                "message":"todo deleted successfully"
            }
        else:
            raise HTTPException(status_code=404,detail="todo not found")
        
            
 




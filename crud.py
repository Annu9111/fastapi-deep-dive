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
    

@router.get("/",response_model=list[todo_response])
def home(db:Session=Depends(get_db)):
    return db.query(todos).all()


@router.post("/",response_model=todo_response) 
def create_todo(todo:TodoCreate,db:Session=Depends(get_db)):
    new_todo = Todo(title=todo.title,description=todo.description,done=todo.done)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

@router.put("/{todo_id}",response_model=todo_response)
def update(todo_id:int,new_todo:TodoCreate,db:Session=Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404,detail="todo not found")
    Todo.title = todo.title
    Todo.description = todo.description
    Todo.done = todo.done
    db.commit()
    return Todo
    

@router.delete("/{todo_id}")
def delete(todo_id:int,db:Session=Depends(get_db)):
    Todo = db.query(Todo).filter(Todo.id==todo_id).first()
    if not Todo:
        return HTTPException(status_code=404,detail="todo not found")
    db.delete(Todo)
    db.commit()
    return{
        "message":"db deleted successfully"
    }
    
    
           
        
            
 




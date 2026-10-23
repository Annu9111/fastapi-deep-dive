from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID, uuid4

app = FastAPI()

class Todo(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    category: str
    status: bool = False

class TodoNameUpdate(BaseModel):
    name: str

db: list[Todo] = []

class BaseOut(BaseModel):
    msg: str
    error: str | None = None

class TodoCreateOut(BaseOut):
    todo: Todo

class TodoGetOut(BaseOut):
    todos: list[Todo]

def find_todo(todo_id: UUID) -> Todo | None:
    for todo in db:
        if todo.id == todo_id:
            return todo
    return None

@app.post("/create", response_model=TodoCreateOut)
def create_todo(todo: Todo):
    db.append(todo)
    return TodoCreateOut(todo=todo, msg="todo created !")

@app.get("/todos", response_model=TodoGetOut)
def fetch_todos():
    return TodoGetOut(todos=db, msg="todos fetched")

@app.get("/todo/{id}", response_model=TodoCreateOut | BaseOut)
def fetch_todo(id: UUID):
    todo = find_todo(id)
    if todo:
        return TodoCreateOut(todo=todo, msg="todo found")
    return BaseOut(msg="todo not found")

@app.put("/update_name/{id}", response_model=TodoCreateOut | BaseOut)
def update_name(id: UUID, data: TodoNameUpdate):
    todo = find_todo(id)
    if todo:
        todo.name = data.name
        return TodoCreateOut(todo=todo, msg="Todo is updated")
    return BaseOut(msg="todo with this id does not exist")

@app.delete("/delete/{id}",response_model=BaseOut)
def delete_todo(id:str)->BaseOut:
    try:
        id = UUID(id)
    except Exception as ex:
        return BaseOut(msg="wrong UUid",error=str(ex))
    
    for i, todo in enumerate(db):
        if todo.id == id:
            del db[i]
            return BaseOut(msg="todo deleted")
    return BaseOut(msg="Todo with UUid is not available")
            
    
from fastapi import FastAPI,APIRouter
from pydantic import BaseModel, Field
from uuid import UUID, uuid4

app = FastAPI()

get_router = APIRouter(prefix="/get",tags=["get route"])
post_router = APIRouter(prefix="/post",tags=["post route"])
put_router = APIRouter(prefix="/put",tags=["put route"])
delete_router = APIRouter(prefix="/delete",tags=["delete route"])

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

@post_router.post("/create", response_model=TodoCreateOut)
def create_todo(todo: Todo):
    db.append(todo)
    return TodoCreateOut(todo=todo, msg="todo created !")

@get_router.get("/todos", response_model=TodoGetOut)
def fetch_todos():
    return TodoGetOut(todos=db, msg="todos fetched")

@get_router.get("/todo/{id}", response_model=TodoCreateOut | BaseOut)
def fetch_todo(id: UUID):
    todo = find_todo(id)
    if todo:
        return TodoCreateOut(todo=todo, msg="todo found")
    return BaseOut(msg="todo not found")

@put_router.put("/update_name/{id}", response_model=TodoCreateOut | BaseOut)
def update_name(id: UUID, data: TodoNameUpdate):
    todo = find_todo(id)
    if todo:
        todo.name = data.name
        return TodoCreateOut(todo=todo, msg="Todo is updated")
    return BaseOut(msg="todo with this id does not exist")

@delete_router.delete("/delete/{id}",response_model=BaseOut)
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

routers=[get_router,post_router,put_router,delete_router]

for router in routers:
    app.include_router(router=router,prefix="/api")
                

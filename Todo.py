# import fast api
from fastapi import FastAPI
from pydantic import BaseModel,Field
from uuid import UUID,uuid4            #uuid4 is used to create unique and random number

#creating fastapi app
app = FastAPI()

#pydantic model for todo
class Todo(BaseModel):
    id : UUID = Field(default_factory=uuid4)
    name:str
    category : str
    status : bool =False

# local variable for todo
db : list[Todo]=[]

# base pydantic mmodel for response
class BaseOut(BaseModel):
    msg:str
    error:str | None


# create route -> used to create new todo
class TodoCreateOut(BaseOut):
    todo:Todo



@app.post("/create",response_model=TodoCreateOut)
def create_todo(todo:Todo)->TodoCreateOut:
    db.append(todo)
    return TodoCreateOut(todo=todo,msg="todo created !")


#get route -> used to fetch todos

class TodoGetout(BaseOut):
    todos:list[Todo]

@app.get("/todos",response_model=TodoGetout)
def fetch_todos():
    return TodoGetout(todos=db,msg="todos fetched")


#get route -> used to fetch a specific todo using its unique id
@app.get("/todo/{id}",response_model=TodoCreateOut | BaseOut)
def fetch_todo(id:str)->TodoCreateOut | BaseOut:
    try:
        id = UUID(id)
    except Exception as ex:
        return BaseOut(msg="Wrong UUid",error=str(ex))
        
            
    
    for todo in db:
        if todo.id == id:
            return TodoCreateOut(todo=todo,msg="todo found")
    return BaseOut(msg="todo not found")

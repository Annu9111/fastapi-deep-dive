# import fast api
from fastapi import FastAPI
from pydantic import BaseModel,Field
from uuid import UUID,uuid4            #uuid4 is used to create unique id using current date and time

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
    error:str = None


# create route -> used to create new todo
class TodoCreateOut(BaseOut):
    todo:Todo



@app.post("/create",response_model=TodoCreateOut)
def create_todo(todo:Todo)->TodoCreateOut:
    db.append(todo)
    return TodoCreateOut(todo=Todo,msg="todo created !")


#get route -> used to fetch todos

class TodoGetout(BaseOut):
    todos:list[Todo]

@app.get("/todos")
def fetch_todos():
    return TodoGetout(todos=db,msg="todos fetched")


    
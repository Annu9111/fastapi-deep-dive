#importing fast api module
from fastapi import FastAPI
from pydantic import BaseModel,ConfigDict

# creating an app of fastapi
app=FastAPI(
    title="Fast api learning docs",
    description="this is my fastapi description box",
    version="0.0.1" 
)

@app.get('/')     #decorator - method - route
def helo():     #api function
    return {'message' : 'hello world from fast api'}

@app.get('/list')
def list_of_val():
    return [1,2,3,4,5,6,5]

@app.post('/create',tags=["Learn"])
def create(data:dict):
    return {"data" : data ,"message":"created"}  

@app.put("/update/{id}")
def update(id:str,data:dict):
    return {"id" : id,"data":data,"msg":"update"}

@app.delete("/deleted/{id}")
def deleted(id:str):
    return {"id":id,"message":"deleted"}

@app.get("/home")
def query_something(q:str):
    return {"q":q,"msg":"query received"}


    
class Post(BaseModel):
    title:str
    description:str
    model_config = ConfigDict(
        extra='forbid'
    )
    
class Post_out(BaseModel):
    post : Post
    msg : str    
    
@app.post("/create_post",response_model=Post_out)
def create_post(post:Post)->Post_out:
    return Post_out(post=Post,msg = "post created")     
        

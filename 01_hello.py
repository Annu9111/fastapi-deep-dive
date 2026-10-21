#importing fast api module
from fastapi import FastAPI

# creating an app of fastapi
app=FastAPI()

@app.get('/')     #decorator - method - route
def helo():     #api function
    return {'message' : 'hello world from fast api'}

@app.get('/list')
def list_of_val():
    return [1,2,3,4,5,6,5]


        
        

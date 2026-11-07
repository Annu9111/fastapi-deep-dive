from fastapi import FastAPI

app = FastAPI()

#home route
@app.get("/")
def home():
    return {"message":"this is a home page route"}

#about route
@app.get("/about")
def about():
    return {"message":"this is aboute route"}

#user route
@app.get("/users")
def user():
    return {"users":["mohit","rohit","ram","shayam"]}


#path parammeters
@app.get("/users/{user_id}")
def get_id(user_id:int):
    return {f"the user id is {user_id}"}

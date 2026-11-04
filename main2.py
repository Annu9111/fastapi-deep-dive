from fastapi import FastAPI

app = FastAPI()

#home route
@app.get("/")
def home():
    return {"message":"this is a home page route"}


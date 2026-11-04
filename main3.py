from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def get_users(name):
    return {"Name":name}

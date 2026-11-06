from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

class UserNotFoundException(Exception):
    def __init__(self, name: str):
        self.name = name

@app.exception_handler(UserNotFoundException)
def user_not_found_handler(request: Request, exc: UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={"status": "error", "message": f"user {exc.name} not found"},
    )

@app.get("/user/id/{user_id}")
def get_user_by_id(user_id: int):
    if user_id != 1:
        raise HTTPException(status_code=404, detail="user not found")
    return {"id": 1, "name": "mohit"}

@app.get("/user/name/{name}")
def get_user_by_name(name: str):
    if name != "mohit":
        raise UserNotFoundException(name)
    return {"name": name}
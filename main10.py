from fastapi import FastAPI,HTTPException

app= FastAPI()

@app.get("/user/{user_id}")
def get_user(user_id:int):
    if user_id!=1:
        raise HTTPException(status_code=404,detail="user not found")
    return {
         "id":1,
         "name":"mohit"
    }

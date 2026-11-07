from fastapi import FastAPI,Depends

app = FastAPI()

#dependency injection

def common_logic():
    return {
        "message":"common logic executed"
    }

@app.get("/home")
def home(data = Depends(common_logic)):
    return data

#second eg:


def get_curr_user():
    return {
        "name":"mohit"
    }

@app.get("/profile/{user_id}")
def profile(user_id : int,user = Depends(get_curr_user)):
    return{
        "id":user_id
    }

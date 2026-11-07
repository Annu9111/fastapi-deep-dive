from fastapi import FastAPI,Depends,Header,HTTPException

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
        "id":user_id,
        "user":user
    }
    
#auth eg:
def verify_token(token:str=Header(None)):
    if token != "Annu":
        raise HTTPException(
            status_code=401,
            detail="unauthorized"
        )

    return {
        "user":"authorized user"
    } 

@app.get("/secure_data")
def secure_data(user=Depends(verify_token)):
    return{
        "message":"secure data accessed",
        "user":user
    }       

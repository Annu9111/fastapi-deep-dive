from fastapi import FastAPI,HTTPException,Depends,Header
from jose import jwt 
from datetime import datetime, timedelta,timezone

app = FastAPI()

SECRET_KEY = "mysecret"

ALGORITHM = "HS256"

#create token
def create_token(data:dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc)+ timedelta(minutes=30)
    to_encode.update({
        "exp":expire
    })
    token = jwt.encode(to_encode,SECRET_KEY,algorithms=ALGORITHM)
    return token

#Login api token
@app.post("/login")
def login(username:str,password:int):
    if username!="annu" and password!="1234":
        raise HTTPException(
            status_code=401,
            detail="invalid username and password"
        )
    token = create_token({
        "sub":username
    })
    return{
        "access_token" : token
    }

#token verify
def token_verify(token:str = Header(None)):
    try:
        payload = jwt.decode(token , SECRET_KEY,algorithms = [ALGORITHM])
        return payload
    except:
        raise HTTPException(
            status_code=401,
            detail="invalid or expire token"
        )

#protected route
@app.get("/secure")
def secure_data(user = Depends(token_verify)):
    return{
        "message":"Secure Data Access",
        "user":user
    }


        
        

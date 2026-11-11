from fastapi import FastAPI, HTTPException, Depends, Header
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext

app = FastAPI()

# jwt config
SECRET_KEY = "mysecret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# password hashing setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# oauth setup
oauth2_schema = OAuth2PasswordBearer(tokenUrl="/login")

# DUMMY User db
fake_user_db = {
    "admin": {
        "username": "admin",
        "hashed_password": pwd_context.hash("123")
    }
}


# hash password
def hash_password(password: str):
    return pwd_context.hash(password)


# verify Password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# create token
def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token


# login api token
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_user_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )
    access_token = create_token({"sub": form_data.username})
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# token verify
def token_verify(authorization: str = Header(None, alias="Authorization")):
    if not authorization or not authorization.lower().startswith("bearer "):
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    token = authorization.split(" ", 1)[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")


# protected route
@app.get("/secure")
def secure_data(user=Depends(token_verify)):
    return {
        "message": "Secure Data Access",
        "user": user
    }
        

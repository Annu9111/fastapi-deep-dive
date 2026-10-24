from fastapi import APIRouter

user_router = APIRouter(prefix="/user",tags=["user"])

@user_router.get("/Signin")
def Signin():
    return {"msg":"user Sign in"}


@user_router.get("/Signup")
def Signup():
    return {"msg":"user Sign up"}



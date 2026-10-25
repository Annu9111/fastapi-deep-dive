from fastapi import FastAPI,Request
from routers import todo_router,user_router

app = FastAPI()

@app.middleware("http")
async def request_detail(request:Request,call_next):
   response= await call_next(request)
   return response 

routers=[todo_router,user_router]



for router in routers:
    app.include_router(router=router,prefix="/api")
                

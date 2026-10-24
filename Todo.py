from fastapi import FastAPI
from routers import todo_router

app = FastAPI()


routers=[todo_router]

for router in routers:
    app.include_router(router=router,prefix="/api")
                

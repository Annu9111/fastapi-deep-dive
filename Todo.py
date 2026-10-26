from fastapi import FastAPI,Request
from routers import todo_router,user_router
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse

app = FastAPI()

limiter = Limiter(key_func=get_remote_address)

app.state.limiter =limiter
app.add_exception_handler(
    RateLimitExceeded,
    lambda request,exc:JSONResponse(
        status_code=429,
        content={
            "detail":"too many request",
        },
    ),
        
)

app.add_middleware(SlowAPIMiddleware)



@app.middleware("http")
async def request_detail(request:Request,call_next):
   response= await call_next(request)
   return response 

routers=[todo_router,user_router]



for router in routers:
    app.include_router(router=router,prefix="/api")
                

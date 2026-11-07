from fastapi import FastAPI,Request

app = FastAPI()

@app.middleware("http")
async def my_middleware(request:Request,call_next):
    print("request received")
    
    response = await call_next(request)
    print ("response sent")
    
    return response
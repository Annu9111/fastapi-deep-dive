from fastapi import FastAPI,Request
import time 

app = FastAPI()

#middleware
@app.middleware("http")
async def my_middleware(request:Request,call_next):
    print("request received")
    
    response = await call_next(request)
    print ("response sent")
    
    return response

#second eg:
@app.middleware("http")
async def log_middleware(request:Request,call_next):
    start_time = time.time()
    
    res = await call_next(request)
    
    end_time = time.time()
    process_time = end_time - start_time
    
    print(f"path: {request.url.path} | time: {process_time}")
    return res
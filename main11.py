from fastapi import FastAPI,Depends

app = FastAPI()

def common_logic():
    return {
        "message":"common logic executed"
    }

@app.get("/home")
def home(data = Depends(common_logic)):
    return data


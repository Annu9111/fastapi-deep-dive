from fastapi import FastAPI

app = FastAPI()


#query parameters
@app.get("/users")
def get_users(name:str=None):
    return {"Name":name}


@app.get("/products")
def get_limit(limit:int = 10):
    return {"limit":limit}

@app.get("/items")
def get_items(name : str = None , price : int = 10):
    return {"name":name , "price":price}

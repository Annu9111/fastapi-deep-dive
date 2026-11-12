# import requests

# response = requests.get("https://jsonplaceholder.typicode.com/posts")

# data = response.json()
# print(data)

from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/post")
def get_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    return response.json()


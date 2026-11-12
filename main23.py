from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/new")
def get_new(page:int=1 , limit:int=5):
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    title = []
    
    for item in soup.find_all("span",class_="titleine"):
        title.append(item.text)
    
    #pagination logic
    start = (page-1)*limit
    end = start+limit
    
    return {
        "page":page,
        "limit":limit,
        "total":len(title),
        "data":title[start:end]
        
    }
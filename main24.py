from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
import time

app = FastAPI()

#cache storage
cache_data=[]
last_fetch = 0

@app.get("/new")
def get_new():
    global cache_data,last_fetch
    
    start = time.time()
    
    if time.time()-last_fetch > 60:
        print("fetching fresh data")
        
        url ="https://news.ycombinator.com/"
        response = requests.get(url)
        
        soup = BeautifulSoup(response.text,"html.parser")
        
        cache_data = [
            item.text for item in soup.find_all("span",class_ = "titleline")
            
        ]
        last_fetch = time.time()
    else:
        print("using chache data")
        
    end  =time.time()
    time_taken = round(end-start)
    
    print("time taken",time_taken)
    return {
        "time taken":time_taken,
        "data":cache_data[:5]
    }
        
    
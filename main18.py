from fastapi import FastAPI, UploadFile,File,HTTPException
from fastapi.staticfiles import StaticFiles
import os
import shutil

app = FastAPI()

#step-1: Ensure upload folder exists
UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

#step-2:Static files setup
app.mount("/files",StaticFiles(directory=UPLOAD_DIR),name="files")

#Step-3:Upload files api
@app.post("/upload")
def upload_file(file:UploadFile=File(...)):
    filename = file.filename
    file_path = os.path.join(UPLOAD_DIR,filename)
    
    if not file:
        raise HTTPException(
            status_code=400,
            detail="file not selected"
        )
    with open(file_path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
        
        return {
            "message":"File uploaded successfuly",
            "file name" :filename,
            "file_url":f"http://127.0.0.1.8000/files/{filename}"
            
        }

#get file url api
@app.get("file/{filename}")
def get_file(filename:str):
    file_path = os.path.join(UPLOAD_DIR,filename)
    
    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=404,
            detail="file not found"
        )    
    return { "file_url":f"http://127.0.0.1.8000/files/{filename}"}

@app.get("/")
def home():
    return {
        "mmessage":"file uploaded api running"
    }

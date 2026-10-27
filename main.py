from fastapi import FastAPI,HTTPException,Path
import json

app = FastAPI()

@app.get("/")         #endpoint-> where on the url the below function should be executed
def greet():
    return {"Welcome to fastAPI course"}

@app.get("/hello")
def hello():
    return {"hello to this hello route"}


def load_data():
    with open("students.json","r") as f:
        return json.load(f)
    
@app.get("/students")
def students():
    return load_data()

@app.get("/students/{student_id}")
def get_id(student_id:str = Path(...,description="the id of the student",example="S001")):
    data = load_data()
    if student_id not in data:
        raise HTTPException(status_code=404,detail=f"student with this {student_id} id does not exists")
    return data[student_id]

@app.get("/filter")
def filter_student(course:str):
    data=load_data()
    
    if course not in data:
        return data
    
    filtered = {}
    for student_id, info in data.items():
        if info["course"]==course:
            filtered[student_id] = info
    return filtered
        
        
    
from fastapi import FastAPI,HTTPException,Path,Query
import json

app = FastAPI()

#get end point
@app.get("/")         #endpoint-> where on the url the below function should be executed
def greet():
    return {"Welcome to fastAPI course"}

@app.get("/hello")
def hello():
    return {"hello to this hello route"}


#function to load data
def load_data():
    with open("students.json","r") as f:
        return json.load(f)

#function to execute loaded data   
@app.get("/students")
def students():
    return load_data()


#path parameter
@app.get("/students/{student_id}")
def get_id(student_id:str = Path(...,description="the id of the student",example="S001")):
    data = load_data()
    if student_id not in data:
        raise HTTPException(status_code=404,detail=f"student with this {student_id} id does not exists")
    return data[student_id]
 
 
#query parameter 
@app.get("/filter")
def filter_student(course:str = Query(None,description="shows only student course",examples=["python"])):
    data=load_data()
    
    if course is None:
        return data
    
    filtered = {}
    for student_id, info in data.items():
        if info["course"].lower()==course.lower():
            filtered[student_id] = info
    return filtered
  
  
SORT_FIELDS = ["marks","age","name"]     
SORT_ORDER = ["asc","desc"]   
@app.get("/sort")
def sort_students(
    sort_by : str =Query(None,description="sort by marks,age,name",examples=["marks"]),
    order : str=Query(None,description="order by asc,desc",examples=["asc"])
    ):
     
    if sort_by not in SORT_FIELDS:
        raise HTTPException(status_code=404,detail=f"invalid sort_by {sort_by}, choose from {SORT_FIELDS}")
    
    if order not in SORT_ORDER:
        raise HTTPException(status_code=404, detail=f"invalid order {order} choose from {SORT_ORDER}")
    
    #now to sort
    data = load_data()
    
    #step1-> turn a dictionary into a listand putting the id inside each student
    student = []
    for stud_id,info in data.items():
        info["id"]=stud_id
        student.append(info)
        
    #step2-> sort the list by the choosen field
    reverse = (order == "desc")
    sorted_student = sorted(student,key = lambda s: s[sort_by],reverse = reverse)
    
    return sorted_student    
    
        
        
        
    
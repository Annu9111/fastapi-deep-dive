from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker,declarative_base,Session 
from fastapi import FastAPI,Depends

app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
)

session_local = sessionmaker(engine)

Base = declarative_base()

class Todo(Base):
    __tablename__="todos"
    
    id = Column(Integer , primary_key=True , index=True)
    title = Column(String)
    completed = Column(String)

Base.metadata.create_all(bind = engine)

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

#create api
@app.post("/todos")
def create_todo(title:str,db:Session=Depends(get_db)):
    todo = Todo(title=title,completed="False")
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return {
        "message":"todo created successfully",
        "data":todo
    }

#read all data
@app.get("/todos")
def get_todos(db:Session=Depends(get_db)):
    todos = db.query(Todo).all()
    
    return {
        "total" : len(todos),
        "data" : todos
    }


@app.get("/todos/{todo_id}")
def get_todo(todo_id:int , db:Session=Depends(get_db)):
    todo = db.query(Todo).filter(todo_id)
    
      
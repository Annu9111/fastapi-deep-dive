from sqlalchemy import Integer,String,Boolean,Column
from database import Base

class Todo(Base):
    __tablename__ = "Todos"
    
    id = Column(Integer,primary_key=True,index=True,nullable=False)
    title = Column(String,index=True)
    description = Column(String,nullable=True)
    done = Column(Boolean,default=False)


    
    
    
    
    
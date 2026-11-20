from sqlalchemy import Integer,String,Boolean,Column

class Todo:
    __tablename__ = "Todos"
    
    id = Column(Integer,primary_key=True,index=True,nullable=False)
    title = Column(String,index=True)
    description = Column(String,nullable=True)
    done = Column(Boolean,default=False)


    
    
    
    
    
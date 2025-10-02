from typing import Optional
from student import Student
from database import JSONDatabase


class StudentController:
    
    def __init__(self, database: JSONDatabase):
        self.database = database
        self.current_student: Optional[Student] = None
    
       
from typing import Optional
from student import Student
from database import JSONDatabase


class StudentController:
    
    def __init__(self, database: JSONDatabase):
        self.database = database
        self.current_student: Optional[Student] = None
    
    def login_test(self, student_id: str) -> bool:
        student_data = self.database.get_student(student_id)
        if student_data:
            self.current_student = Student(**student_data)
            return True
        return False
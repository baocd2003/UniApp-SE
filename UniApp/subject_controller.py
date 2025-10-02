from database import JSONDatabase
from student_controller import StudentController


class SubjectController:
    
    def __init__(self, database: JSONDatabase, student_controller: StudentController):
        self.database = database
        self.student_controller = student_controller

        
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

    def show_enrolled_subject(self):
        if not self.current_student:
            print("No student is currently logged in.")
            return
        data = self.database._read_data()
        students = data.get("students", [])
        subjects = data.get("subjects", [])

        student = next((s for s in students if s.get("email") == self.current_student.email), None)
        if not student:
        print("Student record not found.")
        return

        enrolled_ids = student.get("enrolled_subjects", [])
        if not enrolled_ids:
            print("You have not enrolled in any subjects yet.")
            return

        print("Your enrolled subjects:")
        for subj_id in enrolled_ids:
            subject = next((sub for sub in subjects if sub.get("id") == subj_id), None)
            if subject:
                 print(f"- {subject['name']} (ID: {subject['id']})")

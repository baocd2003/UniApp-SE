from typing import Optional
from student import Student
from database import JSONDatabase

class StudentController:
    
    def __init__(self, database: JSONDatabase):
        self.database = database
        self.current_student: Optional[Student] = None
    
    def login(self, email: str, password: str):
        student_record = self.database.find_student(email, password)

        if student_record is not None:
            self.current_student = Student(
            student_record["id"],
            student_record["name"],
            student_record["email"],
            student_record["password"]
        )
            self.current_student.enrollments = student_record.get("enrollments", [])
            return True
        
        return False
    

    def pass_fail_partition(self):
        students = self.database.get_all_students()

        passed = []
        failed = []
        
        for student in students:
            enrollments = student.get("enrollments", [])
            if not enrollments:
                continue
        
        # Compute Marks
            avg_mark =  sum(sub.get("mark", 0) for sub in enrollments) / len(enrollments)

            if avg_mark >= 50:
                passed.append((student.get("name"), avg_mark))
            else:
                failed.append((student.get("name"), avg_mark))

        print("PASS:")
        if passed:
            for name, avg in passed:
                print(f"{name}")
        else:
            print("No students Passed")
            
        print("FAIL:")
        if failed:
            for name, avg in failed:
                print(f"{name}")
        else:
            print("No students Failed")

    
    def group_by_grade(self):
        students = self.database.get_all_students()
    
        grade_hd = []
        grade_d = []
        grade_c = []
        grade_p = []
        grade_z = []

        for student in students: 
            enrollments = student.get("enrollments", [])
            if not enrollments:
                continue

         # Compute Marks (same logic)
            avg_mark = sum(sub.get("mark", 0) for sub in enrollments) / len(enrollments)

            if avg_mark >= 85:
                grade_hd.append((student.get("name"), avg_mark))
            elif avg_mark >= 75:
                grade_d.append((student.get("name"), avg_mark))
            elif avg_mark >= 65:
                grade_c.append((student.get("name"), avg_mark))
            elif avg_mark >= 50:
                grade_p.append((student.get("name"), avg_mark))
            else:
                grade_z.append((student.get("name"), avg_mark))

        print("\nHD --> ", grade_hd if grade_hd else "[]")
        print("D --> ", grade_d if grade_d else "[]")
        print("C --> ", grade_c if grade_c else "[]")
        print("P --> ", grade_p if grade_p else "[]")
        print("Z --> ", grade_z if grade_z else "[]")      
from typing import Optional
from student import Student
from database import JSONDatabase
import random
import re
from subject import Subject
class StudentController:
    
    def __init__(self, database: JSONDatabase):
        self.database = database
        self.current_student: Optional[Student] = None

    def register_student(self, email: str, password: str) -> bool:
        """Register a new student."""
        # Generate a unique student ID
        student_id = self._generate_unique_student_id()
        
        if not Student._validate_email(email) or not Student._validate_password(password):
            print("Invalid email or password format.")
            return False
        print("email and password format acceptable")
        student_existed = self.is_existed(email)
        if student_existed is not None:
            print(f"Student {student_existed['name']} already exists.")
            return False
        name = input("Enter name: ")
        new_student = Student(student_id, name, email, password)
        self.database.add_student(new_student)
        print(f"Enrolled student {name}")
        return True
    
    def _generate_unique_student_id(self) -> int:
        existing_ids = []
        for student in self.database.get_all_students():
            existing_ids.append(student['id'])
        new_id = random.randint(1, 999)
        while new_id in existing_ids:
            new_id = random.randint(1, 999)
        return new_id
    
    def is_existed(self, email: str) -> Student:
        for student in self.database.get_all_students():
            if student['email'] == email:
                return student
        return None

    def login_student(self, email: str, password: str) -> bool:
        if not email or not password:
            print("Email and password are required.")
            return False
        
        # Find student by email
        student_data = self.is_existed(email)
        if student_data is None:
            print("Student does not exist.")
            return False
        
        # Check password
        if student_data['password'] != password:
            print("Incorrect password.")
            return False
        
        # Convert dictionary to Student object and set as current student
        self.current_student = Student(
            student_data['id'],
            student_data['name'], 
            student_data['email'],
            student_data['password']
        )
        # Load enrollments if they exist
        if 'enrollments' in student_data:
            from subject import Subject
            self.current_student.enrollments = [
                Subject(subj['id'], subj['name']) for subj in student_data['enrollments']
            ]
        
        print(f"Welcome {self.current_student.name}!")
        return True
    
    def logout_student(self):
        
        if self.current_student:
            print(f"Goodbye {self.current_student.name}!")
            self.current_student = None
        else:
            print("No student is currently logged in.")

    def enroll_subject(self) -> bool:
        if self.current_student is None:
            print("No student is currently logged in.")
            return False
        
        if len(self.current_student.enrollments) >= 4:
            print("Students are allowed to enroll in 4 subjects only.")
            return False
        
        
        subject_list = self.database.get_all_subjects()
        
        enrolled_ids = [subject.id for subject in self.current_student.enrollments]
        available_subjects = [s for s in subject_list if s['id'] not in enrolled_ids]
        
        if not available_subjects:
            print("No available subjects to enroll in.")
            return False
        
        random_subject_data = available_subjects[random.randint(0, len(available_subjects)-1)]
        
        new_subject = Subject(random_subject_data['id'], random_subject_data['name'])
        
        self.current_student.enrollments.append(new_subject)
        self.database.update_student(self.current_student)
        
        print(f"Enrolled in {new_subject.name} (ID: {new_subject.id})")
        print(f"Assigned mark: {new_subject.mark}, Grade: {new_subject.grade}")
        print(f"You are now enrolled in {len(self.current_student.enrollments)} out of 4 subjects.")
        return True
    
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
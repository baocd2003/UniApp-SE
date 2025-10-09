import json
import os
from typing import List, Dict, Optional
from student import Student
import student
from subject import Subject

class JSONDatabase:
    
    def __init__(self, filename: str = "student.data.json"):
        self.filename = filename
        self._ensure_file_exists()
    
    def _ensure_file_exists(self):
        if not os.path.exists(self.filename):
            initial_data = {
                "students": [],
                "subjects": [
                    {"id": 541, "name": "Mathematics"},
                    {"id": 455, "name": "Physics"},
                    {"id": 742, "name": "Chemistry"},
                    {"id": 1097, "name": "Biology"},
                    {"id": 764, "name": "Computer Science"},
                    {"id": 97, "name": "English Literature"}
                ]
            }
            with open(self.filename, 'w') as file:
                json.dump(initial_data, file, indent=2)
    
    # Read data from the json file
    def _read_data(self) -> Dict:
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {"students": [], "subjects": []}
    
    # Write data to the json file
    def _write_data(self, data: Dict):
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=2)
    
    # Add subject to the json file
    def add_subject(self, subject):
        data = self._read_data()
        data["subjects"].append({
            "id": subject.id,
            "name": subject.name,
        })
        self._write_data(data)
    
    # Get all subjects from the json file
    def get_all_subjects(self) -> List:
        data = self._read_data()
        return data.get("subjects", [])
    
    def get_all_students(self) -> List:
        data = self._read_data()
        return data.get("students", [])
    
    def add_student(self, student: Student):
        data = self._read_data()
        data["students"].append({
            "id": student.id,
            "name": student.name,
            "email": student.email,
            "password": student.password,
            "enrollments": [
                {
                    "id": subject.id,
                    "name": subject.name,
                    "mark": subject.mark,
                    "grade": subject.grade
                } for subject in student.enrollments
            ] if student.enrollments is not None else []
        })
        self._write_data(data)

    def update_student(self, student: Student):
        data = self._read_data()
        for i, student_data in enumerate(data["students"]):
            if student_data.get("id") == student.id:
                data["students"][i] = {
                    "id": student.id,
                    "name": student.name,
                    "email": student.email,
                    "password": student.password,
                    "enrollments": [
                        {
                            "id": subject.id,
                            "name": subject.name,
                            "mark": subject.mark,
                            "grade": subject.grade
                        } for subject in student.enrollments
                    ] if student.enrollments is not None else []
                }
                break

        self._write_data(data)
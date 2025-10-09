import json
import os
from typing import List, Dict, Optional
from student import Student
from subject import Subject

class JSONDatabase:
    
    def __init__(self, filename: str = "student.data.json"):
        self.filename = filename
        print("DB file =>", os.path.abspath(self.filename))
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
    
     # Return all students as a list of dicts
    def get_all_students(self) -> List[Dict]:
        data = self._read_data()
        return data.get("students", [])

    # Find a student by integer ID; return None if not found
    def find_by_id(self, student_id: int) -> Optional[Dict]:
        for student in self.get_all_students():
            try:
                if int(student.get("id")) == student_id:
                    return student
            except (TypeError, ValueError):
                continue
        return None

    # Update only the student's password; True on success, False if not found
    def update_student_password(self, student_id: int, new_password: str) -> bool:
        data = self._read_data()
        changed = False
        for student in data.get("students", []):
            try:
                if int(student.get("id")) == student_id:
                    student["password"] = new_password
                    changed = True
                    break
            except (TypeError, ValueError):
                continue
        if changed:
            self._write_data(data)
        return changed

    # Remove a student by integer ID; True if removed, False if not found
    def remove_by_id(self, student_id: int) -> bool:
        data = self._read_data()
        original_list = data.get("students", [])
        new_list = []
        for student in original_list:
            try:
                if int(student.get("id")) != student_id:
                    new_list.append(student)
            except (TypeError, ValueError):
                new_list.append(student)
        if len(new_list) == len(original_list):
            return False
        data["students"] = new_list
        self._write_data(data)
        return True

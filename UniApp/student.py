import random
import re
from typing import List, Dict, Any
from subject import Subject


class Student:
    
    def __init__(self, student_id: int, name: str, email: str, password: str):
        self.id = student_id
        self.name = name
        self.email = email
        self.password = password
        self.enrollments: List[Subject] = []
    

        """Create Student instance from dictionary."""
        # Handle missing fields gracefully
        student = cls(
            data.get("id", 0), 
            data.get("name", ""), 
            data.get("email", ""), 
            data.get("password", "")
        )
        student.enrollments = [Subject.from_dict(s) for s in data.get("enrollments", data.get("subjects", []))]
        return student
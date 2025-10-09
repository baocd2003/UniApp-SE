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
    
    @staticmethod
    def _validate_email(email: str) -> bool:
        pattern = r'^[a-zA-Z]+\.[a-zA-Z]+@university\.com$'
        return bool(re.match(pattern, email))
     
    @staticmethod
    def _validate_password(password: str) -> bool:
        pattern = r'^[A-Z][a-zA-Z]{4,}\d{3,}$'
        return bool(re.match(pattern, password))

    


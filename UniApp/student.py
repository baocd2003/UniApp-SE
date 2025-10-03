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
    

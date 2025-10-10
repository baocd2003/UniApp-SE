import random
from typing import Dict, Any


class Subject:
    """Subject class representing a university subject with ID, name, mark, and grade."""
    
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name
        self.mark = random.randint(25, 100)
        self.grade = self.random_grade()

    def random_grade(self):
        if self.mark >= 85:
            return "HD"
        elif self.mark >= 75:
            return "D"
        elif self.mark >= 65:
            return "C"
        elif self.mark >= 50:
            return "P"
        else:
            return "F"

    @staticmethod
    def format_subject_id(subject_id: int) -> str:
        return f"{subject_id:03d}"

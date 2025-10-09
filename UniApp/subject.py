import random
from typing import Dict, Any


class Subject:
    """Subject class representing a university subject with ID, name, mark, and grade."""
    
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.mark = random.randint(0, 100)
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
            return "Z"


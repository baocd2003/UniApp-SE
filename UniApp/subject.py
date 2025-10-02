import random
from typing import Dict, Any


class Subject:
    """Subject class representing a university subject with ID, name, mark, and grade."""
    
    def __init__(self, subject_id: int, name: str, mark: int = None, grade: str = None):
        self.id = subject_id
        self.name = name
        self.mark = mark 
        self.grade = grade
    
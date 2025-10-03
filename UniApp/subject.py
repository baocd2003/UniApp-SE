import random
from typing import Dict, Any


class Subject:
    """Subject class representing a university subject with ID, name, mark, and grade."""
    
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.mark = 0
        self.grade = "Ungraded"


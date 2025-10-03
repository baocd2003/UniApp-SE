import random
from database import JSONDatabase
from student_controller import StudentController
from subject import Subject

class SubjectController:
    
    def __init__(self, database: JSONDatabase, student_controller: StudentController):
        self.database = database
        self.student_controller = student_controller

    # Sample function
    def create_subject(self, name: str) -> Subject:
        subject_id = self._generate_unique_subject_id()
        new_subject = Subject(subject_id, name)
        self.database.add_subject(new_subject)
        return new_subject

    def _generate_unique_subject_id(self) -> int:
        existing_ids = []
        for subject in self.database.get_all_subjects():
            existing_ids.append(subject['id'])

        while True:
            new_id = random.randint(100, 9999)  # Generate random ID between 100 and 9999
            if new_id not in existing_ids:
                return new_id
    
import os
from database import JSONDatabase
from student_controller import StudentController
from subject_controller import SubjectController


class UniApp:
    def __init__(self):
        db_file = os.path.join(os.path.dirname(__file__), "student.data.json")
        self.database = JSONDatabase(filename=db_file)
        self.student_controller = StudentController(self.database)
        self.subject_controller = SubjectController(self.database, self.student_controller)
    
    def run(self):
        while True:
            choice = input("University System: (A)dmin, (S)tudent, or X : ").upper()
            
            if choice == 'X':
                print("Thank You")
                break
            elif choice == 'S':
                # print("Student System")
                self._handle_student_system()
            elif choice == 'A':
                # print("Admin System")
                self._handle_admin_system()
    
        # Student system entry: login then open the student menu
    def _handle_student_system(self):
        """Handle student system operations."""
        while True:
            choice = input("Student System (l/r/x): ").lower().strip()
            if choice == 'x':
                break
            elif choice == 'r':
                print("Registering Student")
            elif choice == 'l':
                if self.student_controller.login():
                    self._handle_student_menu()

    # Student course menu: provides Change Password and placeholders for other actions
    def _handle_student_menu(self):
        """Handle student course menu after successful login."""
        while True:
            choice = input("Student Course Menu (c/e/r/s/x): ").lower().strip()
            if choice == 'x':
                self.student_controller.current_student = None
                break
            elif choice == 'c':
                self.student_controller.change_password()
            elif choice == 'e':
                print("Enrol subject (TBD)")
            elif choice == 'r':
                print("Remove subject (TBD)")
            elif choice == 's':
                print("Show subjects (TBD)")
            else:
                print("Unsupported option.")

    # Admin system: show all students and remove a student by integer ID
    def _handle_admin_system(self):
        """Handle admin system operations."""
        while True:
            choice = input("Admin System (r=remove, s=show, x=exit): ").lower().strip()
            if choice == 'x':
                break
            elif choice == 's':
                students = self.database.get_all_students()
                if not students:
                    print("(no students)")
                else:
                    print("All students:")
                    for student in students:
                        print(f"- ID: {student.get('id')}, Name: {student.get('name')}, Email: {student.get('email')}")
            elif choice == 'r':
                student_id_text = input("Enter student ID (int): ").strip()
                try:
                    student_id = int(student_id_text)
                except ValueError:
                    print("Invalid ID format.")
                    continue
                removed = self.database.remove_by_id(student_id)
                print(f"Student {student_id} removed." if removed else f"Student {student_id} not found.")
            else:
                print("Unsupported option.")


if __name__ == "__main__":
    app = UniApp()
    app.run()
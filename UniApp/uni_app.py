from database import JSONDatabase
from student_controller import StudentController
from subject_controller import SubjectController


class UniApp:
    def __init__(self):
        self.database = JSONDatabase()
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
    
    def _handle_student_system(self):
        """Handle student system operations."""
        while True:
            choice = input("Student System (l/r/x): ").lower()
            
            if choice == 'x':
                break
            elif choice == 'r':
                print("Registering Student")
            elif choice == 'l':
                print("Logging in Student")
    
    def _handle_student_menu(self):
        """Handle student course menu after successful login."""
        while True:
            choice = input("Student Course Menu (c/e/r/s/x): ").lower()
            
            if choice == 'x':
                self.student_controller.current_student = None
                break
            elif choice == 'e':
                print("Enrolling Subject")
            elif choice == 'r':
                print("Removing Subject")
            elif choice == 's':
                print("Showing Subjects")
            elif choice == 'c':
                print("Changing Password")
    
    def _handle_admin_system(self):
        """Handle admin system operations."""
        while True:
            choice = input("Admin System (c/g/p/r/s/x/t): ").lower()
            
            if choice == 'x':
                break
            elif choice == 's':
                print("Showing Students")
            elif choice == 'c':
                print("Clearing Students")
            elif choice == 'g':
                print("Grouping Students")
            elif choice == 'p':
                print("Partitioning Students")
            elif choice == 'r':
                print("Removing Student")
            elif choice == 't':
                subject_name = input("Enter subject name: ")
                new_subject = self.subject_controller.create_subject(subject_name)
                print(f"Created new subject: {new_subject}")

if __name__ == "__main__":
    app = UniApp()
    app.run()
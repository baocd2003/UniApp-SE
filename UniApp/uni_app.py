import os
from database import JSONDatabase
from student_controller import StudentController
from subject_controller import SubjectController
import tkinter as tk
from gui_uni_app import GUIUniApp

class UniApp:
    def __init__(self):
        
        self.database = JSONDatabase()
        self.student_controller = StudentController(self.database)
        self.subject_controller = SubjectController(self.database, self.student_controller)
    
    def run(self):
        while True:
            mode_choice = input("Choose interface: (C)LI or (G)UI or X to exit: ").upper()
            
            if mode_choice == 'X':
                print("Thank You")
                break
            elif mode_choice == 'C':
                self._run_cli_mode()
            elif mode_choice == 'G':
                self._run_gui_mode()
            else:
                print("Invalid choice. Please enter C for CLI, G for GUI, or X to exit.")
    
    def _run_cli_mode(self):
        while True:
            choice = input("University System: (A)dmin, (S)tudent, or X : ").upper()
            
            if choice == 'X':
                break
            elif choice == 'S':
                # print("Student System")
                self._handle_student_system()
            elif choice == 'A':
                # print("Admin System")
                self._handle_admin_system()
    
    def _run_gui_mode(self):
        root = tk.Tk()
        app = GUIUniApp(root)
        root.mainloop()
    
    def _handle_student_system(self):
        """Handle student system operations."""
        while True:
            choice = input("Student System (l/r/x): ").lower().strip()
            if choice == 'x':
                break
            elif choice == 'r':
                self.student_controller.register_student(
                    email=input("Enter email: "),
                    password=input("Enter password: ")
                )
            elif choice == 'l':
                attempts = 3
                for attempt in range(attempts):
                    email = input("Enter email: ")
                    password = input("Enter password: ")
                
                    if not email or not password:
                        print("Please enter both email and password.")
                        continue
                    
                    if self.student_controller.login(email, password):
                        print("Login Successful")
                        self._handle_student_menu()
                    else:
                        print("Invalid email or password, try again")
                else:
                    print("Too many failed attempts. Returning to the Student menu.")           
    
    def _handle_student_menu(self):
        while True:
            choice = input("Student Course Menu (c/e/r/s/x): ").lower().strip()
            if choice == 'x':
                self.student_controller.logout_student()
                self.run()
            elif choice == 'e':
                self.student_controller.enroll_subject()
            elif choice == 'r':
                self.student_controller.remove_subject()
            elif choice == 's':
                self.student_controller.show_enrolled_subject()
            elif choice == 'c':
                self.student_controller.change_password()
    
    def _handle_admin_system(self):
        while True:
            choice = input("Admin System (r=remove, s=show, x=exit): ").lower().strip()
            if choice == 'x':
                break
            elif choice == 's':
                students = self.database.get_all_students()
                if not students:
                    print("(no students)")
                else:
                    print("Student List")
                    for student in students:
                        print(f"{student.get('name')} :: {student.get('id')} --> Email: {student.get('email')}")
            elif choice == 'c':
                self.database.clear_database()
            elif choice == 'g':
                self.student_controller.group_by_grade()
            elif choice == 'p':
                self.student_controller.pass_fail_partition()
            elif choice == 'r':
                self.student_controller.remove_student()
            elif choice == 't':
                subject_name = input("Enter subject name: ")
                new_subject = self.subject_controller.create_subject(subject_name)
                print(f"Created new subject: {new_subject}")

if __name__ == "__main__":
    app = UniApp()
    app.run()

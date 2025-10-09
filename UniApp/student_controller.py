import re
from typing import Optional
from student import Student
from database import JSONDatabase

EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+-]+@[Uu][Nn][Ii][Vv][Ee][Rr][Ss][Ii][Tt][Yy]\.com$")
PWD_RE   = re.compile(r"^[A-Z][A-Za-z]{4,}\d{3,}$")  # First letter uppercase + >=5 letters + >=3 digits

class StudentController:
    # Initialize controller; keep database handle and current logged-in student
    def __init__(self, database: JSONDatabase):
        self.database = database
        self.current_student: Optional[Student] = None

    # Log in with integer student_id and password; construct a runtime Student on success
    def login(self) -> bool:
        student_id_text = input("Student ID: ").strip()
        try:
            student_id = int(student_id_text)
        except ValueError:
            print("Invalid ID.")
            return False

        password = input("Password: ").strip()
        record = self.database.find_by_id(student_id)
        if not record:
            print("Login failed. (reason: student not found)")
            return False
        if record.get("password") != password:
            print("Login failed. (reason: wrong password)")
            return False

        self.current_student = Student(record["id"], record["name"], record["email"], record["password"])
        print(f"Welcome, {self.current_student.name}!")
        return True

    # Student menu after login (includes Change Password; others are placeholders)
    def menu(self):
        if self.current_student is None:
            print("Please login first.")
            return
        while True:
            choice = input("(c) change  (e) enrol  (r) remove  (s) show  (x) exit : ").lower().strip()
            if choice == "x":
                break
            elif choice == "c":
                self.change_password()
            elif choice == "e":
                print("Enrol subject (TBD)")
            elif choice == "r":
                print("Remove subject (TBD)")
            elif choice == "s":
                print("Show subjects (TBD)")
            else:
                print("Unsupported option.")

    # Change the current logged-in student's password (persist only the password field)
    def change_password(self):
        if self.current_student is None:
            print("No student is logged in.")
            return

        print("Change password")
        while True:
            new_password = input("Enter new password: ").strip()
            if not PWD_RE.match(new_password):
                print("Invalid password format. It must start with an uppercase letter, contain at least five letters, and be followed by three or more digits.")
                retry = input("Try again? (y/n): ").lower().strip()
                if retry != "y":
                    return
                continue

            confirm = input("Confirm new password: ").strip()
            if confirm != new_password:
                print("Passwords do not match.")
                continue

            self.current_student.password = new_password
            updated = self.database.update_student_password(self.current_student.id, new_password)
            print("Password updated successfully." if updated else "Failed to update password. Please try again.")
            return

       
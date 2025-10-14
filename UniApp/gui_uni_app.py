import tkinter as tk
from tkinter import messagebox
from database import JSONDatabase
from student_controller import StudentController

class GUIUniApp:
    def __init__(self, root):
        self.root = root
        self.root.title("UniApp - Login")
        self.root.geometry("800x600")
        self.root.resizable(True, True)

        # Connect to existing database and controller
        self.database = JSONDatabase()
        self.controller = StudentController(self.database)

        self.login_attempts = 0

        self._login_window()

    def _login_window(self):
        tk.Label(self.root, text="Welcome to UniApp", font=("Arial", 16, "bold")).pack(pady=15)
        tk.Label(self.root, text="Email:", font=("Arial", 12)).pack()
        self.email_entry = tk.Entry(self.root, width=30)
        self.email_entry.pack(pady=5)

        tk.Label(self.root, text="Password:", font=("Arial", 12)).pack()
        self.password_entry = tk.Entry(self.root, width=30, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self.root, text="Login", width=15, command=self._handle_login).pack(pady=15)
        tk.Button(self.root, text="Exit", width=15, command=self.root.quit).pack()

    def _handle_login(self):
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()

        if not email or not password:
            messagebox.showerror("Error", "Please enter both email and password.")
            return

        success = self.controller.login(email, password)

        if success:
            messagebox.showinfo("Login Successful", "Login Successful")
            self.login_attempts = 0  # reset
        
        else:
            self.login_attempts += 1

        if self.login_attempts < 3:
            messagebox.showerror("Login Failed", "Invalid email or password, try again")
        else:
            messagebox.showwarning("Too Many Attempts", "Too many failed attempts. Returning to the Student menu.")
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = GUIUniApp(root)
    root.mainloop()

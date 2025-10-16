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
    # Login sceen 
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
    # Handle Login 
    def _handle_login(self):
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()

        if not email or not password:
            messagebox.showerror("Error", "Please enter both email and password.")
            return

        success = self.controller.login(email, password, True)

        if success:
            messagebox.showinfo("Login Successful", "Login Successful")
            self.login_attempts = 0 
            self._show_student_menu()
        
        else:
            self.login_attempts += 1
            if self.login_attempts >= 3:
                messagebox.showwarning("Too Many Attempts", "Too many failed attempts. Returning to the Student menu.")
                self.root.quit()
            else:
                messagebox.showerror("Login Failed", "Invalid email or password, try again")

    # Student Menu
    def _show_student_menu(self):
        # Clear the login window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.root.title("UniApp - Student Menu")
        
        # Welcome message
        welcome_label = tk.Label(self.root, text=f"Welcome {self.controller.current_student.name}!", 
                                font=("Arial", 16, "bold"))
        welcome_label.pack(pady=20)
        
        # Student Course Menu title
        menu_title = tk.Label(self.root, text="Student Course Menu", 
                             font=("Arial", 14, "bold"))
        menu_title.pack(pady=10)
        
        # Menu buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)
        
        # Enroll in Subject button
        enroll_btn = tk.Button(button_frame, text="Enroll in Subject (e)", 
                              width=25, height=2, font=("Arial", 10),
                              command=self._handle_enroll_subject)
        enroll_btn.pack(pady=5)
        
        # Remove Subject button
        remove_btn = tk.Button(button_frame, text="Remove Subject (r)", 
                              width=25, height=2, font=("Arial", 10),
                              command=self._handle_remove_subject)
        remove_btn.pack(pady=5)
        
        # Show Enrolled Subjects button
        show_btn = tk.Button(button_frame, text="Show Enrolled Subjects (s)", 
                            width=25, height=2, font=("Arial", 10),
                            command=self._handle_show_subjects)
        show_btn.pack(pady=5)
        
        # Change Password button
        change_pwd_btn = tk.Button(button_frame, text="Change Password (c)", 
                                  width=25, height=2, font=("Arial", 10),
                                  command=self._handle_change_password)
        change_pwd_btn.pack(pady=5)
        
        # Logout button
        logout_btn = tk.Button(button_frame, text="Logout (x)", 
                              width=25, height=2, font=("Arial", 10),
                              bg="#ff6b6b", fg="white",
                              command=self._handle_logout)
        logout_btn.pack(pady=15)

    # Enroll in Subject
    def _handle_enroll_subject(self):
        success = self.controller.enroll_subject(isGui=True)
        if success:
            self._refresh_student_info()

    # Remove Subject
    def _handle_remove_subject(self):
        if not self.controller.current_student.enrollments:
            messagebox.showinfo("No Subjects", "No subjects to remove.")
            return
        
        # Create a dialog to select subject to remove
        self._show_remove_subject_dialog()

    # Show Removable Subject Dialog
    def _show_remove_subject_dialog(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Remove Subject")
        dialog.geometry("400x300")
        dialog.grab_set()  # Make dialog modal
        
        tk.Label(dialog, text="Select a subject to remove:", 
                font=("Arial", 12, "bold")).pack(pady=10)
        
        # Create listbox with enrolled subjects
        listbox_frame = tk.Frame(dialog)
        listbox_frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        scrollbar = tk.Scrollbar(listbox_frame)
        scrollbar.pack(side="right", fill="y")
        
        subject_listbox = tk.Listbox(listbox_frame, yscrollcommand=scrollbar.set, 
                                    font=("Arial", 10))
        subject_listbox.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=subject_listbox.yview)
        
        # Populate listbox with enrolled subjects
        enrollments = self.controller.current_student.enrollments
        for i, subject in enumerate(enrollments):
            display_text = f"Subject {subject.id} - {subject.name} (Mark: {subject.mark}, Grade: {subject.grade})"
            subject_listbox.insert(i, display_text)
        
        # Buttons
        button_frame = tk.Frame(dialog)
        button_frame.pack(pady=10)
        
        def remove_selected():
            selection = subject_listbox.curselection()
            if not selection:
                messagebox.showwarning("No Selection", "Please select a subject to remove.")
                return
            
            selected_index = selection[0]
            selected_subject = enrollments[selected_index]
            
            success = self.controller.remove_subject(str(selected_subject.id), isGui=True)
            if success:
                dialog.destroy()
                self._refresh_student_info()
        
        tk.Button(button_frame, text="Remove Selected", command=remove_selected,
                 bg="#ff6b6b", fg="white", width=15).pack(side="left", padx=5)
        tk.Button(button_frame, text="Cancel", command=dialog.destroy,
                 width=15).pack(side="left", padx=5)

    # Show Enrolled Subjects
    def _handle_show_subjects(self):
        enrollments = self.controller.show_enrolled_subject(isGui=True)
        
        if not enrollments:
            return  # Message already shown by controller
        
        # Create a dialog to display subjects
        dialog = tk.Toplevel(self.root)
        dialog.title("Enrolled Subjects")
        dialog.geometry("500x400")
        dialog.grab_set()
        
        tk.Label(dialog, text=f"Enrolled Subjects ({len(enrollments)} of 4)", 
                font=("Arial", 14, "bold")).pack(pady=10)
        
        # Create text widget with scrollbar
        text_frame = tk.Frame(dialog)
        text_frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side="right", fill="y")
        
        text_widget = tk.Text(text_frame, yscrollcommand=scrollbar.set, 
                             font=("Arial", 10), wrap="word")
        text_widget.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=text_widget.yview)
        
        # Display subject information
        for subject in enrollments:
            subject_info = f"Subject ID: {subject.id}\n"
            subject_info += f"Subject Name: {subject.name}\n"
            subject_info += f"Mark: {subject.mark}\n"
            subject_info += f"Grade: {subject.grade}\n"
            subject_info += "-" * 40 + "\n\n"
            text_widget.insert("end", subject_info)
        
        text_widget.config(state="disabled")  # Make read-only
        
        tk.Button(dialog, text="Close", command=dialog.destroy, width=15).pack(pady=10)

    # Change Password
    def _handle_change_password(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Change Password")
        dialog.geometry("350x250")
        dialog.grab_set()
        
        tk.Label(dialog, text="Change Password", font=("Arial", 14, "bold")).pack(pady=15)
        
        tk.Label(dialog, text="New Password:", font=("Arial", 10)).pack()
        new_pwd_entry = tk.Entry(dialog, width=30, show="*")
        new_pwd_entry.pack(pady=5)
        
        tk.Label(dialog, text="Confirm Password:", font=("Arial", 10)).pack()
        confirm_pwd_entry = tk.Entry(dialog, width=30, show="*")
        confirm_pwd_entry.pack(pady=5)
        
        def change_password():
            new_password = new_pwd_entry.get().strip()
            confirm_password = confirm_pwd_entry.get().strip()
            
            if not new_password or not confirm_password:
                messagebox.showerror("Error", "Please fill in both password fields.")
                return
            
            success = self.controller.change_password(new_password, confirm_password, isGui=True)
            if success:
                dialog.destroy()
        
        button_frame = tk.Frame(dialog)
        button_frame.pack(pady=15)
        
        tk.Button(button_frame, text="Update Password", command=change_password,
                 bg="#4CAF50", fg="white", width=15).pack(side="left", padx=5)
        tk.Button(button_frame, text="Cancel", command=dialog.destroy,
                 width=15).pack(side="left", padx=5)

    # Logout
    def _handle_logout(self):
        self.controller.logout_student(isGui=True)
        
        # Clear the menu and return to login
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.root.title("UniApp - Login")
        self.login_attempts = 0
        self._login_window()


if __name__ == "__main__":
    root = tk.Tk()
    app = GUIUniApp(root)
    root.mainloop()

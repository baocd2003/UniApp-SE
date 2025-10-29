# UniApp - University Management System

UniApp is a student management system that allows students to register, login, and manage their course enrollments at a university. The application supports both CLI (Command-Line Interface) and GUI (Graphical User Interface) modes.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [How to Run](#how-to-run)
  - [CLI Mode](#cli-mode)
  - [GUI Mode](#gui-mode)
- [Function Use Cases](#function-use-cases)
  - [Student System](#student-system)
  - [Admin System](#admin-system)
- [Email and Password Requirements](#email-and-password-requirements)
- [File Structure](#file-structure)

---

## Features

- **Dual Interface**: Choose between CLI and GUI
- **Student Management**: Register, login, and manage enrollments
- **Course Management**: Enroll in and remove subjects
- **Admin Tools**: Manage students, subjects, and grades
- **Data Persistence**: All data stored in JSON format
- **Input Validation**: Email and password format validation

---

## Installation

### Prerequisites

- Python 3.7 or higher
- tkinter (usually included with Python)

### Setup

1. Clone or download the project to your local machine:
   ```bash
   git clone <repository-url>
   cd UniApp
   ```

2. No external dependencies are required. The application uses only Python's standard library.

---

## How to Run

### Starting the Application

Run the main application file:

```bash
python uni_app.py
```

You will be prompted to choose an interface:

```
Choose interface: (C)LI or (G)UI or X to exit: 
```

---

## CLI Mode

### Accessing CLI Mode

1. Start the application: `python uni_app.py`
2. Select **C** for CLI mode
3. Choose your role: **S** (Student) or **A** (Admin)

### Student System (CLI)

```
Student System (l/r/x): 
```

#### Available Options:

| Option | Function | Description |
|--------|----------|-------------|
| **r** | Register | Register as a new student |
| **l** | Login | Login with your email and password |
| **x** | Exit | Return to main menu |

#### After Login - Student Course Menu:

```
Student Course Menu (c/e/r/s/x): 
```

| Option | Function | Description |
|--------|----------|-------------|
| **e** | Enroll in Subject | Add a course to your enrollment list |
| **r** | Remove Subject | Drop a course from your enrollment |
| **s** | Show Enrolled Subjects | View all your enrolled courses |
| **c** | Change Password | Update your account password |
| **x** | Logout | Exit student menu and return to main menu |

### Admin System (CLI)

```
Admin System (c/g/p/r/s/x/t): 
```

#### Available Options:

| Option | Function | Description |
|--------|----------|-------------|
| **s** | Show Students | View all registered students |
| **c** | Create Subject | Add a new subject/course to the system |
| **g** | Generate Subject Report | Generate a report of all subjects |
| **p** | Generate Pass Report | Generate a pass rate report for subjects |
| **r** | Report | Generate general reports |
| **t** | Test Subject | Test subject functionality |
| **x** | Exit | Return to main menu |

---

## GUI Mode

### Accessing GUI Mode

1. Start the application: `python uni_app.py`
2. Select **G** for GUI mode
3. A window will open with the login interface

### GUI Login Screen

- Enter your email and password
- Click **Login** button to proceed
- Click **Exit** button to close the application

### GUI Student Menu

After successful login, you'll see a menu with the following buttons:

| Button | Function | Description |
|--------|----------|-------------|
| **Enroll in Subject (e)** | Enroll | Select and enroll in an available course |
| **Remove Subject (r)** | Remove | Drop an enrolled course |
| **Show Enrolled Subjects (s)** | View Courses | Display all your enrolled courses |
| **Change Password (c)** | Change Password | Update your account password |

---

## Email and Password Requirements

### Email Format

Emails must follow this pattern:
```
[firstname].[lastname]@university.com
```

**Example:** `john.smith@university.com`

**Rules:**
- First name: letters only
- Last name: letters only
- Must end with `@university.com`

### Password Format

Passwords must meet the following criteria:
```
[Uppercase][4+ letters][3+ digits]
```

**Example:** `Hello1234`, `Welcome123`

**Rules:**
- Must start with an uppercase letter
- Followed by at least 4 lowercase letters
- Must contain at least 3 digits
- Minimum length: 8 characters

---

## Function Use Cases

### Student System

#### 1. **Register Student**
   - **Use Case**: Create a new student account
   - **Input**: Email (format: firstname.lastname@university.com), Password, Name
   - **Validation**: Email and password must follow required formats
   - **Output**: Confirmation message with student ID
   - **File Modified**: `student.data.json`

#### 2. **Login Student**
   - **Use Case**: Authenticate student account
   - **Input**: Email, Password
   - **Validation**: Max 3 failed attempts
   - **Output**: Access to student menu or error message
   - **Note**: Limited to 3 login attempts

#### 3. **Enroll in Subject**
   - **Use Case**: Register for a course
   - **Process**: 
     1. System displays available subjects
     2. Student selects a subject by ID
     3. Course is added to student's enrollment list
   - **Output**: Confirmation message or error if already enrolled

#### 4. **Remove Subject**
   - **Use Case**: Drop an enrolled course
   - **Process**:
     1. System displays student's enrolled subjects
     2. Student selects a subject to remove
     3. Course is deleted from enrollment list
   - **Output**: Confirmation message

#### 5. **Show Enrolled Subjects**
   - **Use Case**: View all current course enrollments
   - **Output**: List of all subjects the student is enrolled in
   - **Note**: Empty list if no courses enrolled

#### 6. **Change Password**
   - **Use Case**: Update account password
   - **Process**:
     1. Verify current password
     2. Enter new password
     3. Password updated in database
   - **Input Validation**: New password must follow password requirements
   - **Output**: Confirmation or error message

### Admin System

#### 1. **Create Subject**
   - **Use Case**: Add a new course to the system
   - **Input**: Subject name
   - **Process**: Generates unique subject ID and stores in database
   - **Output**: Confirmation with subject ID
   - **File Modified**: `student.data.json`

#### 2. **Show Students**
   - **Use Case**: Display all registered students
   - **Output**: List of all students with their details (ID, Name, Email)
   - **Use Case**: Database management and verification

#### 3. **Generate Subject Report**
   - **Use Case**: View all available subjects
   - **Output**: Complete list of subjects with their IDs and names
   - **Default Subjects**: 
     - Mathematics (541)
     - Physics (455)
     - Chemistry (742)
     - Biology (1097)
     - Computer Science (764)
     - English Literature (97)

#### 4. **Generate Pass Report**
   - **Use Case**: Analyze subject pass rates
   - **Output**: Report showing pass statistics for each subject
   - **Use Case**: Academic performance analysis

#### 5. **Test Subject**
   - **Use Case**: System testing and debugging
   - **Purpose**: Internal testing functionality

#### 6. **Report**
   - **Use Case**: Generate general system reports
   - **Output**: Summary statistics and database information

---

## File Structure

```
UniApp/
├── uni_app.py                 # Main entry point - CLI/GUI selector
├── gui_uni_app.py             # GUI interface implementation
├── student.py                 # Student class definition
├── student_controller.py       # Student business logic
├── subject.py                 # Subject class definition
├── subject_controller.py       # Subject business logic
├── database.py                # JSON database management
├── student.data.json          # Data storage (auto-created)
└── README.md                  # This file
```

---

## Data Storage

All data is stored in `student.data.json` with the following structure:

```json
{
  "students": [
    {
      "id": "000001",
      "name": "John Smith",
      "email": "john.smith@university.com",
      "password": "HashedPassword",
      "enrollments": [541, 455]
    }
  ],
  "subjects": [
    {
      "id": 541,
      "name": "Mathematics"
    }
  ]
}
```

---

## Troubleshooting

### Email Validation Error
- Ensure email follows format: `firstname.lastname@university.com`
- Only letters allowed in name portions

### Password Validation Error
- Ensure password starts with uppercase letter
- Contains at least 4 lowercase letters
- Contains at least 3 digits

### Login Failed (Too Many Attempts)
- After 3 failed login attempts, you must restart the application
- Check your email and password carefully

### GUI Not Opening
- Ensure tkinter is installed: `python -m tkinter`
- Try CLI mode instead

---

## Default Credentials

To test the system, you can register a new account with:

- **Email**: `test.user@university.com`
- **Password**: `Test1234` or `Admin1234` (must follow the format)
- **Name**: Your choice

---

## Support

For issues or questions, please refer to the code comments or contact the development team.

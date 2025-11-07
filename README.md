# Student Course Management System

## 1. Project Overview

This is a console-based application built in Python to manage student records, covering all required CRUD (Create, Read, Update, Delete) operations.

The system utilizes **Object-Oriented Programming (OOP)**, a **dictionary data structure** (`self.students`), and robust **exception handling** to ensure a reliable user experience.

### Implemented Features (Required & Bonus)

| Category | Feature | Status |
| :--- | :--- | :--- |
| **Required** | Add, Remove, Update, View All, Search by Name | Complete |
| **Required** | Load/Save Data to **JSON** (`students.json`) | Complete |
| **Bonus (+3 Marks)**| Export to **CSV** format (`students.csv`) | Complete |
| **Technical** | Columnar Display for View All Students (Improved Readability) | Complete |
| **Technical** | Exception Handling (`try/except`) for file operations and inputs | Complete |

## 2. Setup and Installation

### Prerequisites

You must have Python 3 (version 3.6 or newer) installed on your system.

### Dependencies

This project uses only modules included in the Python Standard Library (`json`, `csv`, `sys`). No external libraries are needed.

## 3. How to Run the Program

1.  **Save Files:** Ensure your Python script (e.g., `student.py`) and the data file (`students.json`) are saved in the same directory the one you specified: 
2.  **Open Terminal/Command Prompt:** Navigate to the project directory.
3.  **Execute the Script:** Run the program using the Python interpreter:

    ```bash
    python student.py
    ```
    

## 4. Using the Program and Data Files

Upon startup, the system automatically attempts to **Load Data (Option 7)** from `students.json`.

### Recommended First Steps

1.  **Load Data:** Select **Option 7** to load the provided 18 sample student records.
2.  **View Data:** Select **Option 4** to view the student list displayed in a clean, columnar format.

### File Handling (Option 6)

Option 6 is a sub-menu for data saving and exporting:

* **Choice 'a' (Save to JSON):** Saves the current state of student records to `students.json`.
* **Choice 'b' (Export to CSV):** Creates a file named **`students.csv`** in the project folder, which is perfect for viewing the data in a spreadsheet program like Excel (secures the +3 bonus).
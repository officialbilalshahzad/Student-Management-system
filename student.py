import json
import sys # Used for potential graceful exit
import csv

class Student:
    
    
    def __init__(self, student_id, name, age, course, marks):
        """Initializes a new Student object with required attributes."""
        self.student_id = student_id 
        self.name = name 
        self.age = age 
        self.course = course 
        self.marks = marks 

    def __str__(self):
        """Returns a string representation of the student for easy viewing."""
        return (f"ID: {self.student_id} | Name: {self.name} | Age: {self.age} | "
                f"Course: {self.course} | Marks: {self.marks}")
    
    def to_dict(self):
        """Converts the Student object into a standard Python dictionary for JSON """
        # Required for "File handling (read/write JSON)"
        return {
            "id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "marks": self.marks
        }


# Manages the dictionary of student records and all CRUD operations.
class StudentManager:
    def __init__(self):
        """Initializes the manager, using a dictionary for fast ID lookups."""
        # Mandatory "dictionary to store student data"
        self.students = {} 
        self.load_data_from_file() # Auto-load data on startup

    # --- Menu Option 1: Add Student ---
    def add_student(self): 
        print("\n--- 1. Add New Student ---")
        student_id = input("Enter Student ID: ")
        
        # Check for ID redundancy (bonus robustness)
        if student_id in self.students:
            print(f"\n Error: Student ID {student_id} already exists.")
            return

        name = input("Enter Student Name: ")
        course = input("Enter Course Name: ")
        
        # Mandatory "Exception handling using try/except" for input conversion
        try:
            # Safely convert input to int and float
            age = int(input("Enter Age (e.g., 20): "))
            marks = float(input("Enter Marks (e.g., 85.5): "))
            
        except ValueError:
            print("\n Input Error: Age and Marks must be numerical. Student not added.")
            return 
            
        # Create and Store the Student Object (OOP)
        new_student = Student(student_id, name, age, course, marks)
        self.students[student_id] = new_student
        
        print(f"\n✅ Success! Student {name} ({student_id}) added.")
        
    # --- Menu Option 2: Remove Student ---
    def remove_student(self):
        print("\n--- 2. Remove Student ---")
        id_to_remove = input("Enter the Student ID to remove: ")
        
        # Check if the ID exists in the dictionary keys
        if id_to_remove in self.students:
            del self.students[id_to_remove]
            print(f"\n Success! Student with ID {id_to_remove} removed.")
        else:
            print(f"\n Error: Student ID {id_to_remove} not found.")

    # --- Menu Option 3: Update Student ---
    def update_student(self):
        print("\n--- 3. Update Student Record ---")
        id_to_update = input("Enter the Student ID to update: ")

        if id_to_update not in self.students:
            print(f"\n Error: Student ID {id_to_update} not found. Nothing updated.")
            return

        student = self.students[id_to_update] 
        print(f"\nFound Student: {student}")
        
        print("\nWhich attribute would you like to update?")
        print("a. Name | b. Age | c. Course | d. Marks | e. Cancel")
        choice = input("Enter your choice (a-e): ").lower()

        if choice == 'a':
            new_name = input(f"Enter New Name (current: {student.name}): ")
            student.name = new_name
            print(f" Name updated successfully to {new_name}.")
 
        elif choice == 'b':
            new_age_input = input(f"Enter New Age (current: {student.age}): ")
            try:
                new_age = int(new_age_input)
                student.age = new_age
                print(f" Age updated successfully to {new_age}.")
            except ValueError:
                print(" Invalid input. Age must be a whole number. Update failed.")
        
        elif choice == 'c':
            new_course = input(f"Enter New Course (current: {student.course}): ")
            student.course = new_course
            print(f"✅ Course updated successfully to {new_course}.")

        elif choice == 'd':
            new_marks_input = input(f"Enter New Marks (current: {student.marks}): ")
            try:
                new_marks = float(new_marks_input)
                student.marks = new_marks
                print(f" Marks updated successfully to {new_marks}.")
            except ValueError:
                print(" Invalid input. Marks must be a number (e.g., 85.5). Update failed.")

        elif choice == 'e':
            print("Update cancelled.")
        else:
            print("Invalid option selected.")

    # --- Menu Option 4: View All Students ---
    
    def view_all_students(self):
        print("\n--- 4. All Enrolled Students ---")
        
        if not self.students:
            print("No students are currently enrolled in the system.")
            return

        # 1. Print the Header Row with Alignment
        header = (
            f"{'ID':<5} "        # Left-aligned, 5 characters wide
            f"{'NAME':<20} "     # Left-aligned, 20 characters wide
            f"{'AGE':^5} "       # Center-aligned, 5 characters wide
            f"{'COURSE':<25} "    # Left-aligned, 25 characters wide
            f"{'MARKS':>5}"       # Right-aligned, 5 characters wide
        )
        print("-" * len(header))
        print(header)
        print("-" * len(header))

        # 2. Iterate and print data rows
        for student_obj in self.students.values():
            data_row = (
                f"{student_obj.student_id:<5} "
                f"{student_obj.name:<20} "
                f"{student_obj.age:^5} "
                f"{student_obj.course:<25} "
                f"{student_obj.marks:>5.1f}" 
            )
            print(data_row)
            
        print("-" * len(header))

    # --- Menu Option 5: Search Student by Name ---
    def search_student_by_name(self):
        print("\n--- 5. Search Student ---")
        search_term = input("Enter name or part of a name to search: ")
        found_students = []
        
        # Case-insensitive search using .lower() and 'in' (Advanced Python)
        for student_obj in self.students.values():
            if search_term.lower() in student_obj.name.lower():
                found_students.append(student_obj)

        if found_students:
            print(f"\n Found {len(found_students)} student(s) matching '{search_term}':")
            for student in found_students:
                print(student)
        else:
            print(f"\n No student found matching '{search_term}'.")
    
    # --- Menu Option 6: Save Data to File (File Handling) ---
    def save_data_to_file(self, filename="students.json"):
        # List Comprehension: Converts all Student objects to simple dictionaries
        data_to_save = [student.to_dict() for student in self.students.values()]
        
        try:
            # 'with' statement ensures the file is closed safely
            with open(filename, 'w') as f:
                json.dump(data_to_save, f, indent=4) # Saves data with clean indentation
            
            print(f"\n Success! Student data saved to {filename}.")
            
        except IOError:
            print(f"\n Error: Could not write data to file {filename}.")

    # --- Menu Option 7: Load Data from File (File Handling) ---
    def load_data_from_file(self, filename="students.json"):
        try:
            with open(filename, 'r') as f:
                data_from_file = json.load(f) # Reads data from JSON file
            
            self.students.clear()

            # Loop through simple dictionaries and re-create Student objects (OOP)
            for student_dict in data_from_file:
                new_student = Student(
                    student_dict['id'],
                    student_dict['name'],
                    student_dict['age'],
                    student_dict['course'],
                    student_dict['marks']
                )
                self.students[new_student.student_id] = new_student
            
            print(f"\n✅ Success! Loaded {len(self.students)} student records from {filename}.")

        # Mandatory Error Handling for File Operations
        except FileNotFoundError:
            # This is fine for first run
            print(f"\n Warning: Data file {filename} not found. Starting with an empty system.")
        except json.JSONDecodeError:
            print(f"\n Error: Could not read data from {filename}. File may be corrupt.")
        except Exception as e:
            print(f"\n An unexpected error occurred during loading: {e}")

    #for exporting the csv file
    def export_to_csv(self, filename="students.csv"):
        print(f"\n--- Exporting Data to {filename} ---")
        
        # Define the field names (column headers)
        fieldnames = ['id', 'name', 'age', 'course', 'marks']
        
        try:
            # Open the file in write mode ('w'). newline='' prevents extra blank rows in CSV.
            with open(filename, 'w', newline='') as csvfile:
                # Use DictWriter because our student.to_dict() returns a dictionary
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                # Write the header row
                writer.writeheader()
                
                # Iterate over student objects and write rows
                for student_obj in self.students.values():
                    # We use the existing to_dict() method to get the data as a dictionary
                    writer.writerow(student_obj.to_dict())
            
            print(f" Success! Data successfully exported to {filename}.")
            
        except IOError:
            print(f" Error: Could not write data to file {filename}.")

#  Main Program Flow 

        
def display_menu():
    """Prints the main menu options for the user."""
    print("\n--- Student Course Management System ---")
    print("1. Add Student | 2. Remove Student | 3. Update Student")
    print("4. View All Students | 5. Search Student by Name")
    print("6. Save Data to File | 7. Load Data from File")
    print("8. Exit")
    print("--------------------------------------")


def main():
    """The main entry point of the program, handling the menu loop."""
    manager = StudentManager() 
    running = True 
    
    # Mandatory "Menu should loop until user chooses Exit"
    while running:
        display_menu()
        
        # General Error Handling for unexpected issues
        try:
            choice = input("Enter your choice (1-8): ")
            
            # --- Connecting all 8 Menu Options ---
            if choice == '1':
                manager.add_student() 
            elif choice == '2':
                manager.remove_student()
            elif choice == '3':
                manager.update_student()
            elif choice == '4':
                manager.view_all_students()
            elif choice == '5':
                manager.search_student_by_name()
            elif choice == '6':
                print("\n--- Data Saving Options ---")
                print("a. Save to JSON (students.json)")
                print("b. Export to CSV (students.csv)")
                print("c. Back to Main Menu")
                save_choice = input("Enter your save choice (a-c): ").lower()

                if save_choice == 'a':
                    manager.save_data_to_file()  # Calls the original JSON save
                elif save_choice == 'b':
                    manager.export_to_csv()      # Calls your NEW CSV export function
                elif save_choice == 'c':
                    print("Returning to main menu.")
                else:
                    print("Invalid option. Returning to main menu.")

# --- End of Corrected Block ---
            elif choice == '7':
                manager.load_data_from_file()

            elif choice == '8':
                print("\nSaving data before exiting...")
                manager.save_data_to_file() # Good practice to save on exit
                print("Exiting the Student Management System. Goodbye!")
                running = False 
                
            else:
                print("Invalid choice. Please enter a number between 1 and 8.")
                
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Program continuing.")

# Ensures main() is only called when the script is executed directly
if __name__ == "__main__":
    main()
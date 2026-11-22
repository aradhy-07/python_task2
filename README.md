- List of Lists: students is a list of lists, where each inner list stores one student's name, roll number, and marks.

- Variables: Variables like name, roll, marks, found, and avg store data during program execution.

- Functions: Functions like add_student(), view_students(), search_student(), and average_marks() divide the program into smaller, reusable parts.

- Loops: while loop is used to repeatedly display the menu until the user exits, and for loop is used to iterate through student records.

- Conditional Statements: if, elif, and else are used to execute different operations based on the user's choice and to search for students.

- File Handling: open(), read, write, and close() are used to save student records in a file and retrieve them later, even after restarting the program.

- String Functions: strip() removes unwanted newline characters, and split() separates the data stored in a file using commas.

- Type Conversion: float() and str() are used to convert data between strings and numerical values when storing and retrieving student marks.

- User Input and Output: input() is used to take information from the user, and print() is used to display the menu, student records, and results.

  # Student Management System

## About the Project
This is a menu-driven Student Management System developed using Python. It allows users to add student records, view all students, search for a student using their roll number, and view their marks. Student records are saved in a file so that the data remains available even after the program is closed.

## Features
- Add a student with name, roll number, and marks.
- View all saved student records.
- Search a student by roll number.
- Display a student's marks.
- Save student records permanently in a text file.
- Simple menu-driven interface.

## Python Concepts Used
- Lists and list of lists
- Functions
- Loops (`for` and `while`)
- Conditional statements (`if`, `elif`, `else`)
- File handling
- String methods (`strip()` and `split()`)
- Type conversion (`float()` and `str())
- User input and output

## How to Run the Project
1. Install Python on your computer.
2. Download or clone this project.
3. Open the project folder in VS Code or any Python IDE.
4. Run the Python file.
5. Select an option from the displayed menu.
6. Follow the instructions to manage student records.

## Data Storage
Student records are stored in `students.txt`. The program reads saved records when it starts and appends new student records to the file, allowing the data to persist between executions.

## Author
Aaradhya Garg


def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = float(input("Enter marks: "))

    students.append([name, roll, marks])

    file = open("students.txt", "a")
    file.write(name + "," + roll + "," + str(marks) + "\n")
    file.close()

    print("Student added successfully!")


def view_students():
    if len(students) == 0:
        print("No students found.")
    else:
        for student in students:
            print("Name:", student[0])
            print("Roll Number:", student[1])
            print("Marks:", student[2])
            print("-------------------")


def search_student():
    roll = input("Enter roll number to search: ")
    found = False

    for student in students:
        if student[1] == roll:
            print("Name:", student[0])
            print("Roll Number:", student[1])
            print("Marks:", student[2])
            found = True

    if found == False:
        print("Student not found.")


def average_marks():
    roll = input("Enter roll number: ")
    found = False

    for student in students:
        if student[1] == roll:
            avg = student[2]
            print("Average marks:", avg)
            found = True

    if found == False:
        print("Student not found.")


# Load previously saved students
students = []

file = open("students.txt", "a") #only to ensure  file exist if not it will be created 
file.close()

file = open("students.txt", "r")

for line in file:
    data = line.strip().split(",")
    #strip will remove the \n and split(",") will split the line when it found , 
    students.append([data[0], data[1], float(data[2])])

file.close()


# Main menu
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add student")
    print("2. View all students")
    print("3. Search student by roll number")
    print("4. Calculate average marks")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        average_marks()

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")
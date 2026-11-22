name = input("Enter student name: ")
marks = input("Enter marks: ")

with open("student_data.txt", "w") as file:
    file.write(f"Name: {name}\nMarks: {marks}\n")

with open("student_data.txt", "r") as file:
    print(file.read())

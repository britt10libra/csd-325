import json

with open("Student.json", "r") as student_file:
    students = json.load(student_file)

def print_students(student_list):
    for student in student_list:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']}, Email = {student['Email']}")

print("Original Student List:")
print_students(students)

students.append({
    "F_Name": "Brittany",
    "L_Name": "Smith",
    "Student_ID": 12345,
    "Email": "brittanysmith@gmail.com"
})

print("\nUpdated Student List:")
print_students(students)

with open("Student.json", "w") as student_file:
    json.dump(students, student_file, indent=4)

print("\nThe Student.json file has been updated.")
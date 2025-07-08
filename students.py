
import json
import re


COURSES = ["BCA", "BBA", "B.Tech", "MBA"]
FILE = "data/students.json"

def register_student():
    print("\n--- Register Student ---")
    while True:
        name = input("Name: ")
        if len(name) < 2 or not name.isalpha():
            print("Error: Invalid name. Must be at least 2 letters and alphabetic only.")
        else:
            break

    while True:
        reg_number = input("Registration Number (e.g. REG-2025-0001): ")
        if not re.match(r"^REG-\d{4}-\d{4}$", reg_number):
            print("Error: Invalid registration number format. Must be like REG-2025-0001.")
        else:
            break

    while True:
        try:
            age = int(input("Age: "))
            if 18 <= age <= 25:
                break
            else:
                print("Error: Age must be between 18 and 25.")
        except ValueError:
            print("Error: Age must be a number.")

    while True:
        email = input("Email: ")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("Error: Invalid email format.")
        else:
            break

    while True:
        phone = input("Phone Number: ")
        if not re.match(r"^\d{10}$", phone):
            print("Error: Phone number must be exactly 10 digits.")
        else:
            break

    while True:
        course = input(f"Course ({', '.join(COURSES)}): ")
        if course not in COURSES:
            print("Error: Course must be one of: " + ", ".join(COURSES))
        else:
            break

 
    student = {
        "name": name,
        "reg_number": reg_number,
        "age": age,
        "email": email,
        "phone": phone,
        "course": course
    }


    try:
        with open(FILE, "r") as f:
            students = json.load(f)
    except:
        students = []

    students.append(student)
    with open(FILE, "w") as f:
        json.dump(students, f, indent=4)
    print("Student registered successfully!")

def list_students():
    print("\n--- Student List ---")
    try:
        with open(FILE, "r") as f:
            students = json.load(f)
    except: 
        print("No students found.")
        return

    for i, student in enumerate(students, start=1):
        print(f"{i}. {student['name']} - {student['reg_number']} - {student['course']}")

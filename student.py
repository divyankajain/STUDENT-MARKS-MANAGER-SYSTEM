from validation import get_valid_marks
from grade import get_grade

def add_student(students):
    name = input("Enter student name: ")
    total = 0

    for i in range(1, 4):
        marks = get_valid_marks(i)
        total += marks

    percentage = total / 3
    grade = get_grade(percentage)

    student = {
        "name": name,
        "total": total,
        "percentage": percentage,
        "grade": grade
    }

    students.append(student)
    print("Student added successfully!")

def show_students(students):
    if len(students) == 0:
        print("No students added yet")
        return

    print("\nName\t\tTotal\tPercentage\tGrade")
    print("-" * 45)

    for s in students:
        print(
            s["name"], "\t\t",
            s["total"], "\t",
            round(s["percentage"], 2), "\t\t",
            s["grade"]
        )

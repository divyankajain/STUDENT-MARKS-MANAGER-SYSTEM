students = []

while True:
    print("\n===== STUDENT MARKS MANAGER =====")
    print("1. Add student")
    print("2. show all students")
    print("3. show topper")
    print("4. show class average")
    print("5. exit")

    choice = input("enter your choice:")

    if choice == "1":
        name = input("enter student name :")
        total = 0

        for i in range(1, 4):
            marks = int(input("enter marks of subject" + str(i) + ":"))

            while marks < 0 or marks > 100:
                print("marks should be between 0 and 100")
                marks = int(input("enter marks again:"))

            total = total + marks
            percentage = total / 3

            if percentage >= 90:
                grade = "A+"
            elif percentage >= 75:
                grade = "A"
            elif percentage >= 60:
                grade = "B"
            elif percentage >= 40:
                grade = "C"
            else:
                grade = "Fail"

        student = {
            "name": name,
            "total": total,
            "percentage": percentage,
            "grade": grade
        }

        students.append(student)
        print("student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students added yet")
        else:
            print("Name\tTotal\tPercentage\tGrade")
            for s in students:
                print(s["name"], s["total"], round(s["percentage"], 2), s["grade"])

    elif choice == "3":
        if len(students) == 0:
            print("No students added yet")
        else:
            topper = students[0]

            for s in students:
                if s["total"] > topper["total"]:
                    topper = s

            print("topper is", topper["name"], "with", topper["total"], "marks")

    elif choice == "4":
        if len(students) == 0:
            print("No students added yet")
        else:
            total = 0

            for s in students:
                total = total + s["percentage"]

            average = total / len(students)
            print("class average is", round(average, 2), "%")

    elif choice == "5":
        print("thank you!")
        break

    else:
        print("invalid choice, try again")

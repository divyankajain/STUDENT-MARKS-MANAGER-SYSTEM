def class_average(students):
    if len(students) == 0:
        print("No students added yet")
        return

    total = 0

    for student in students:
        total += student["percentage"]

    average = total / len(students)
    print("Class average is", round(average, 2), "%")

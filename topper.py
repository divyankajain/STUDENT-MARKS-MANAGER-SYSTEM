def show_topper(students):
    if len(students) == 0:
        print("No students added yet")
        return

    topper = students[0]

    for student in students:
        if student["total"] > topper["total"]:
            topper = student

    print(
        "Topper is",
        topper["name"],
        "with",
        topper["total"],
        "marks"
    )

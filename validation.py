def get_valid_marks(subject_number):
    marks = int(input(
        "Enter marks of subject " + str(subject_number) + " (out of 100): "
    ))

    while marks < 0 or marks > 100:
        print("Marks should be between 0 and 100")
        marks = int(input("Enter marks again: "))

    return marks

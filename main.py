from student import add_student
from topper import show_topper
from average import class_average
from student import show_students

def main():
    students = []

    while True:
        print("\n===== STUDENT MARKS MANAGER =====")
        print("1. Add student")
        print("2. Show all students")
        print("3. Show topper")
        print("4. Show class average")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_students(students)
        elif choice == "3":
            show_topper(students)
        elif choice == "4":
            class_average(students)
        elif choice == "5":
            print("Thank you!")
            break
        else:
            print("Invalid choice, try again")

if __name__ == "__main__":
    main()

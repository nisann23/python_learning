#main
import student
import database
import operations

def display_menu():
    print("\n Student Management System ")
    print("1. Add a new student")
    print("2. View all students")
    print("3. Calculate average grade")
    print("4. Exit")
   

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            name = input("Enter student name: ")
            try:
                grade = float(input("Enter student grade: "))
                new_student = student.create_student(name, grade)
                database.add_student(new_student)
            except ValueError:
                print("Invalid grade. Please enter a number.")

        elif choice == '2':
            all_students = database.get_all_students()
            if not all_students:
                print("No students have been added yet.")
            else:
                print("\n List of All Students ")
                for s in all_students:
                    print(f"Name: {s['name']}, Grade: {s['grade']}")

        elif choice == '3':
            all_students = database.get_all_students()
            average = operations.calculate_average_grade(all_students)
            print(f"\nTotal students: {len(all_students)}")
            print(f"The average grade is: {average:.2f}")

        elif choice == '4':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
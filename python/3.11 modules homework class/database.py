# database.py

students_list = []

def add_student(student):
 
    students_list.append(student)
    print(f"Added student: {student['name']}")

def get_all_students():

    return students_list
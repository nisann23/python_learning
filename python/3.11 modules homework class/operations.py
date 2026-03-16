#operations
def calculate_average_grade(students):
    if not students:
        return 0.0
        
    total_grade = 0
    for student in students:
        total_grade += student['grade']
        
    average = total_grade / len(students)
    return average
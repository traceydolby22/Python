import json 

with open("students.json", "r") as s:
    students = json.load(s)

def get_student_names_by_subject(students):
 # Group enrolled student names by subject
    # {"Math": ["Maya Chen", ...], "Science": [...], ...}
    # Only include enrolled students
    subject_to_add = {}
    for student in students:
        subject = student["subject"]
        if student["status"] == "enrolled":
            if subject not in subject_to_add:
                subject_to_add[subject] = []
            subject_to_add[subject].append(student["student"])
    return subject_to_add

print(get_student_names_by_subject(students))
 
def get_name_of_student_with_highest_score(students):
 # Return the name of the enrolled student
    # with the highest score
    highest_score = 0 
    name_of_student = ""
    for student in students:
        score = student["score"]
        name = student["student"]
        if score > highest_score: 
            highest_score = score
            name_of_student = name
    return name_of_student
    
print(get_name_of_student_with_highest_score(students))

def get_average_score_per_grade(students):
# Return average score per grade
    # across ALL students regardless of status
    # rounded to 2 decimal places
    # {10: 80.0, 11: ..., 12: ...}
    grade_to_add = {}
    score_to_add = {}
    for student in students: 
        grade = student["grade"]
        score = student["score"]
        if grade not in grade_to_add: 
            grade_to_add[grade] = 0
            score_to_add[grade] = 0
        grade_to_add[grade] += score
        score_to_add[grade] += 1
    result = {}
    for grade in grade_to_add:
        result[grade] = round(grade_to_add[grade] / score_to_add[grade], 2)
    return result

print(get_average_score_per_grade(students))
    
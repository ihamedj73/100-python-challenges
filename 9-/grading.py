student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}


# - Scores 91 - 100: Grade = "Outstanding"

# - Scores 81 - 90: Grade = "Exceeds Expectations"

# - Scores 71 - 80: Grade = "Acceptable"

# - Scores 70 or lower: Grade = "Fail"


student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score <= 70:
        student_grades[student] = "Fail"
    elif score <= 80:
        student_grades[student] = "Acceptable"
    elif score <= 90:
        student_grades[student] = "Exceeds Expectations"
    else:
        student_grades[student] = "Outstanding"


print(student_scores)
print(student_grades)

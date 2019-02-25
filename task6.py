student_ID = [1, 2, 3, 4, 5]
subject_1 = [89, 90, 78, 93, 80]
subject_2 = [90, 91, 85, 88, 86]

print("student_ID:", student_ID)
for i, j in zip(subject_1, subject_2):
    print((i + j) / 2, end=" ")

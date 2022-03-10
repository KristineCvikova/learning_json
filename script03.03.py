import json

file = open("students.json")
data = json.load(file)
print(data)

for student in data["Students"]:
    print(f"{student['FirstName']} {student['LastName']}")

count = 0
total_age = 0
for student in data["Students"]:
    total_age += int(student["Age"])
    count += 1
print(f"Average age: {total_age/count}")

count_age_group_1 = 0
count_age_group_2 = 0
count_age_group_3 = 0

total_grade_age_group_1 = 0
total_grade_age_group_2 = 0
total_grade_age_group_3 = 0

for student in data["Students"]:
    if int(student["Age"]) <20:
        count_age_group_1 += 1
        total_grade_age_group_1 += int(student["Grade"])

    elif int(student["Age"]) <30:
        count_age_group_2 += 1
        total_grade_age_group_2 += int(student["Grade"])

    else:
        count_age_group_3 += 1
        total_grade_age_group_3 += int(student["Grade"])

print(f"Age group 1 average grade: {total_grade_age_group_1/count_age_group_1}")
print(f"Age group 1 average grade: {total_grade_age_group_2/count_age_group_2}")
print(f"Age group 1 average grade: {total_grade_age_group_3/count_age_group_3}")

count_female = 0
count_male = 0

total_age_female = 0
total_age_male = 0
total_grade_female = 0
total_grade_male = 0

for student in data["Students"]:
    if student["Gender"] == "Female":
        count_female += 1
        total_age_female += int(student["Age"])
        total_grade_female += int(student["Grade"])
    elif student["Gender"] == "Male":
        count_male += 1
        total_age_male += int(student["Age"])
        total_grade_male += int(student["Grade"])

print(f"Female average age: {total_age_female/count_female}")
print(f"Female average grade: {total_grade_female/count_female}")
print(f"Male average age: {total_age_male/count_male}")
print(f"Male average grade: {total_grade_male/count_male}")
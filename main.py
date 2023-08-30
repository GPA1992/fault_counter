import csv
import os
from import_all import import_csv_files
import json

with open("all_students.json", "r") as json_file:
    all_students = json.load(json_file)

all_day_count = import_csv_files("./all_days")

days_with_presence = []


def presence_counter(call_path, present_students):
    parts = call_path.split("_")
    day_type = parts[-1].split(".")[0]
    day = os.path.splitext(call_path)[0]
    presence = []
    for student in all_students:
        if student["student"] in present_students:
            presence.append((student["student"], student["enrollment"], 0))
        else:
            if day_type == "unica":
                presence.append((student["student"], student["enrollment"], 1))
            else:
                presence.append((student["student"], student["enrollment"], 2))
    days_with_presence.append((day, presence))


for day in all_day_count:
    presence_counter(day[0], day[1])

with open("test.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)

sorted_data_array = sorted(days_with_presence, key=lambda item: item[0])


print(sorted_data_array[0])


all_students_set = set()
for _, student_data in sorted_data_array:
    for student, registration, _ in student_data:
        all_students_set.add(student)


header = ["Student", "Registration"]
for date, _ in sorted_data_array:
    header.append(date)


student_dict = {
    student: {
        "Student": student,
        "Registration": "",
        **{date: "" for date, _ in sorted_data_array},
    }
    for student in all_students_set
}

for date, student_data in sorted_data_array:
    for student, registration, presence in student_data:
        student_dict[student][date] = presence
        student_dict[student]["Registration"] = registration


with open("relatorio_final.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    for student_data in student_dict.values():
        writer.writerow(student_data)

print("CSV file created successfully!")

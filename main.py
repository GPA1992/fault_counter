import csv
import os
from import_all import import_csv_files
import json

with open("todos_alunos.json", "r") as arquivo_json:
    todos_alunos = json.load(arquivo_json)


all_day_count = import_csv_files("./all_days")

days_whit_presenca = []


def contador_presenca(chamada_path, alunos_presenca):
    parts = chamada_path.split("_")
    tipo_dia = parts[-1].split(".")[0]
    dia = os.path.splitext(chamada_path)[0]
    presenca = []
    for aluno in todos_alunos:
        if aluno["aluno"] in alunos_presenca:
            presenca.append((aluno["aluno"], 0))
        else:
            if tipo_dia == "unica":
                presenca.append((aluno["aluno"], 1))
            else:
                presenca.append((aluno["aluno"], 2))
    days_whit_presenca.append((dia, presenca))


for day in all_day_count:
    contador_presenca(day[0], day[1])


with open("teste.csv", "w", newline="") as arquivo_csv:
    escritor = csv.writer(arquivo_csv)


all_students = set()
for _, student_data in days_whit_presenca:
    for student, _ in student_data:
        all_students.add(student)

# Crie o cabeçalho do CSV
header = ["Aluno", "Matrícula"]
for date, _ in days_whit_presenca:
    header.append(date)

# Crie um dicionário para armazenar os dados dos alunos
student_dict = {
    student: {"Aluno": student, "Matrícula": ""} for student in all_students
}

# Preencha o dicionário com as informações de cada data
for date, student_data in days_whit_presenca:
    for student, matricula in student_data:
        student_dict[student][date] = matricula

# Escreva os dados no arquivo CSV
with open("output.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    for student_data in student_dict.values():
        writer.writerow(student_data)

print("Arquivo CSV criado com sucesso!")

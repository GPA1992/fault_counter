import csv
import os
from import_all import import_csv_files

all_day_count = import_csv_files("./all_days")


todos_alunos_path = "todos_alunos.csv"
""" chamada_path = "05_10_2023_unica.csv" """

""" parts = chamada_path.split("_")
tipo_dia = parts[-1].split(".")[0]

dia = os.path.splitext(chamada_path)[0] """


todos_alunos = []


def read_todos_alunos():
    with open(todos_alunos_path, encoding="utf8") as file:
        graduacao_reader = csv.reader(file, delimiter=",", quotechar='"')
        next(graduacao_reader)
        for row in graduacao_reader:
            todos_alunos.append(row[0])


def chamada(chamada_path):
    alunos = []
    with open(chamada_path, encoding="utf8") as file:
        graduacao_reader = csv.reader(file, delimiter=",", quotechar='"')
        next(graduacao_reader)
        for row in graduacao_reader:
            alunos.append(row[0])


read_todos_alunos()
""" chamada() """


def contador_presenca(chamada_path, alunos):
    parts = chamada_path.split("_")
    tipo_dia = parts[-1].split(".")[0]
    dia = os.path.splitext(chamada_path)[0]

    output_file_path = "todos_alunos_com_presenca.csv"

    with open(todos_alunos_path, encoding="utf8") as input_file, open(
        output_file_path, "w", encoding="utf8"
    ) as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)

        header = next(reader)
        if dia not in header:
            header.append(dia)

        writer.writerow(header)
        for aluno in reader:
            if aluno[0] in alunos:
                aluno.append(0)
            else:
                if tipo_dia == "unica":
                    aluno.append(1)
                else:
                    aluno.append(2)
            writer.writerow(aluno)


for day in all_day_count:
    contador_presenca(day[0], day[1])

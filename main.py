import csv
import os


todos_alunos_path = "todos_alunos.csv"
chamada_path = "05_10_2023_unica.csv"

parts = chamada_path.split("_")
tipo_dia = parts[-1].split(".")[0]

dia = os.path.splitext(chamada_path)[0]


todos_alunos = []
chamada_alunos = []


def read_todos_alunos():
    with open(todos_alunos_path, encoding="utf8") as file:
        graduacao_reader = csv.reader(file, delimiter=",", quotechar='"')
        next(graduacao_reader)
        for row in graduacao_reader:
            todos_alunos.append(row[0])


def chamada():
    with open(chamada_path, encoding="utf8") as file:
        graduacao_reader = csv.reader(file, delimiter=",", quotechar='"')
        next(graduacao_reader)
        for row in graduacao_reader:
            chamada_alunos.append(row[0])


read_todos_alunos()
chamada()


def contador_presenca():
    output_file_path = "todos_alunos_com_presenca.csv"

    with open(todos_alunos_path, encoding="utf8") as input_file, \
         open(output_file_path, "w", newline="", 
              encoding="utf8") as output_file:

        reader = csv.reader(input_file)
        writer = csv.writer(output_file)

        header = next(reader)
        header.append(dia)
        writer.writerow(header)

        for aluno in reader:
            if aluno[0] in chamada_alunos:
                aluno.append(0)
            else:
                if tipo_dia == 'unica':
                    aluno.append(1)
                else:
                    aluno.append(2)
            writer.writerow(aluno)


contador_presenca()

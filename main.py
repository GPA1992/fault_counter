import csv

with open("08-08-2023-unico.csv", encoding="utf8") as file:
    graduacao_reader = csv.reader(file, delimiter=",", quotechar='"')
    # Usando o conceito de desempacotamento
    header, *data = graduacao_reader

print(data[0])

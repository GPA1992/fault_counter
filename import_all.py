import os
import csv


def import_csv_files(path):
    """
    Importa todos os arquivos CSV de uma pasta e armazena eles em uma lista de
    tuplas.

    Args:
      path: O caminho para a pasta que contém os arquivos CSV.

    Returns:
      Uma lista de tuplas com os dados dos arquivos CSV.
    """

    files = os.listdir(path)
    data = []
    for file in files:
        if file.endswith(".csv"):
            with open(os.path.join(path, file), "r") as f:
                reader = csv.reader(f)
                data.append((file, list(reader)))
    return data


if __name__ == "__main__":
    path = "./all_days"
    data = import_csv_files(path)
    print(data[0])

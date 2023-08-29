import os
import csv


def import_csv_files(path):
    files = os.listdir(path)
    data = []
    for file in files:
        if file.endswith(".csv"):
            with open(os.path.join(path, file), "r") as f:
                reader = csv.reader(f)
                names = [row[0] for row in reader]
                data.append((file, names))
    return data


if __name__ == "__main__":
    path = "./all_days"
    data = import_csv_files(path)
    print(data[0])

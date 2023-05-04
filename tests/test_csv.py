import csv
import os
from conftest import RESOURCES_PATH

# TODO оформить в тест, добавить ассерты и использовать универсальный путь
def test_csv():
    csv_path = os.path.join(RESOURCES_PATH, 'eggs.csv')
    rows = [['Anna', 'Pavel', 'Peter'], ['Alex', 'Serj', 'Yana']]
    with open(csv_path, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        for row in rows:
            csvwriter.writerow(row)


    with open('resources/eggs.csv') as csvfile:
        csvreader = csv.reader(csvfile)
        rows_from_csv = []
        for row in csvreader:
            print(row)
            if row != []:
                rows_from_csv.append(row)
        print(rows)
        assert rows == rows_from_csv
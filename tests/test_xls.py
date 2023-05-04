import os

import xlrd

from conftest import RESOURCES_PATH


# TODO оформить в тест, добавить ассерты и использовать универсальный путь

def test_xls():
    xls_path = os.path.join(RESOURCES_PATH, 'file_example_XLS_10.xls')
    book = xlrd.open_workbook(xls_path)
    print(f'Количество листов {book.nsheets}')
    print(f'Имена листов {book.sheet_names()}')
    sheet = book.sheet_by_index(0)
    print(f'Количество столбцов {sheet.ncols}')
    print(f'Количество строк {sheet.nrows}')
    print(f'Пересечение строки 9 и столбца 1 = {sheet.cell_value(rowx=0, colx=1)}')
    # печать всех строк по очереди
    for rx in range(sheet.nrows):
        print(sheet.row(rx))

    assert 8 == sheet.ncols
    assert 10 == sheet.nrows
    assert 'First Name' == sheet.cell_value(rowx=0, colx=1)
import csv
from openpyxl import load_workbook


def load_gain_from_excel(path, sheetname, lo, hi):
    """ Загрузка коэффициентов усиления из excel"""
    wb = load_workbook(path, data_only=True)
    sheet = wb[sheetname]
    result = []
    for cellobj in sheet[lo:hi]:
        for cell in cellobj:
            result.append(cell.value)
    return result


def save_as(path, what, fmt=None):
    for i, item in enumerate(what):
        with open(path + f'/k{i}.txt', "w") as f:
            for row in item:
                if fmt == 'hex':
                    row = hex(row)
                f.write(row)


def to_csv(filename, data, mode='w'):
    with open(filename, mode) as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(data)

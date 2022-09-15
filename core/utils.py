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


def load_potentiometer_gain(path):
    res = []
    with open(path, 'r') as f:
        for line in f:
            line = line.strip('\n ,')
            res.extend([float(x) for x in line.split(',')])
    return res


def to_csv(filename, data, mode='w'):
    with open(filename, mode) as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(data)


if __name__ == "__main__":
    path = "../data/dp_gains.txt"
    print(load_potentiometer_gain(path))

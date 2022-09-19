# -*- coding: utf-8 -*-

import csv
from openpyxl import Workbook, load_workbook


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


def to_csv(filename, data, mode='w', newline=''):
    with open(filename, mode, newline=newline) as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(data)


def to_excel(filename, data, headers=None):
    wb = Workbook()
    ws = wb.active
    
    if headers:
        ws.append(headers)

    for row in data:
        ws.append(row)

    wb.save(filename)


if __name__ == "__main__":
    to_excel("", [])
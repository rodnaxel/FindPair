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


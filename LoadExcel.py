import openpyxl


def load(paralist, filename):
    workbook = openpyxl.load_workbook(filename)
    sheet = workbook['Sheet1']
    paralist = sheet[1]

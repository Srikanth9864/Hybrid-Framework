import xlrd
from Library.config import Config


def read_locators(sheetname):
    """returns the headers of the testcase in comma seperated string"""
    wb = xlrd.open_workbook(Config.OBJECTS_FILE_PATH)
    ws = wb.sheet_by_name(sheetname)
    total_rows = ws.nrows
    objects = {}
    for index in range(1, total_rows):
        row = ws.row_values(index)
        objects[row[0]] = (row[1], row[2])
    return objects


def read_headers(sheetname, testcase):
    """Returns a dictionary with field name as key and locator type and locator value as value (tuple)"""
    wb = xlrd.open_workbook(Config.DATA_FILE_PATH)
    ws = wb.sheet_by_name(sheetname)
    total_rows = ws.nrows
    for index in range(total_rows):
        row = ws.row_values(index)
        if row[0] == testcase:
            headers = ws.row_values(index - 1, 2)
            return ",".join([header for header in headers if header])


def read_data(sheetname, testcase):
    """Returns a list of tuples"""
    wb = xlrd.open_workbook(Config.DATA_FILE_PATH)
    ws = wb.sheet_by_name(sheetname)
    total_rows = ws.nrows
    final_data = []
    for index in range(total_rows):
        row = ws.row_values(index)
        if row[0] == testcase:
            data = ws.row_values(index, 1)
            data = [item for item in data if item]
            if data[0].lower() == "yes":
                final_data.append(tuple(data[1:]))
    return final_data

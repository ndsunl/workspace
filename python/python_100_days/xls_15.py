from openpyxl import Workbook, load_workbook

def main():
    """
    读取 Excel
    """
    wb = load_workbook('/home/sun/workspace/xls/example.xlsx')
    ws = wb.active

    for row in ws:
        for cell in row:
            print(cell.value)
        print('=== End of Row ===')


if __name__ == '__main__':
    main()
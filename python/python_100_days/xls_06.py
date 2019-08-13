import openpyxl


def main():
    # 指定行列给单元格赋值
    wb = openpyxl.Workbook()
    ws = wb.active

    ws.title = 'WorkSheetTitle'

    # 指定行列给单元格赋值
    ws.cell(row=4, column=2, value=10)

    wb.save('example.xlsx')


if __name__ == '__main__':
    main()
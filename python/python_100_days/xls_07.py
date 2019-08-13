import openpyxl


def main():
    # 给指定范围的单元格赋值
    wb = openpyxl.Workbook()
    ws = wb.active

    ws.title = 'WorkSheetTitle'

    v = 0
    for i in range(1, 10):
        for n in range(1, 10):
            ws.cell(row=i, column=n, value=v)
            v += 1

    wb.save('example.xlsx')

if __name__ == '__main__':
    main()
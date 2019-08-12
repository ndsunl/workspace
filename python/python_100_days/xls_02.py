import openpyxl

if __name__ == '__main__':

    wb = openpyxl.Workbook()
    # 当前打开页
    ws = wb.active

    # 更改默认名称
    ws.title = 'WorkSheetTitle'

    # 保存
    wb.save('example.xlsx')
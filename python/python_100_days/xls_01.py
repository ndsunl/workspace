import openpyxl

if __name__ == '__main__':

    # 创建一个空的 Excel
    wb = openpyxl.Workbook()

    # 保存
    wb.save('example.xlsx')
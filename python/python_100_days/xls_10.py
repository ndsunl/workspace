import openpyxl


def main():
    """
    设置字体
    """
    wb = openpyxl.Workbook()
    ws = wb.active

    ws.title = "WorkSheelTitle"

    font = openpyxl.styles.Font(
        name="微软简老宋",
        size=15,
    )
    a1 = ws['A1']
    a1.font = font
    a1.value = 'TEST'

    wb.save('example.xlsx')


if __name__ == '__main__':
    main()
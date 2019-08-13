import openpyxl

def main():
    # sheel 页标签颜色变更
    wb = openpyxl.Workbook()
    ws = wb.active

    # 更改当前页名称
    ws.title = "WorkSheetTitle"

    # 页标签颜色设定
    ws.sheet_properties.tabColor = "1072BA"

    # 保存
    wb.save("example.xlsx")


if __name__ == "__main__":
    main()
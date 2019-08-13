import openpyxl


# 列名
column_title = ["FirstName", "LastName"]


def main():
    """
    Cell放入值
    """
    wb = openpyxl.Workbook()
    ws = wb.active

    ws.title = "WorkSheetTitle"

    # 追加赋值
    rows = [
        column_title,
        ["Tarou", "Tanaka"],
        ["Tarou", "Suzuki"],
        ["Tarou", "Uchiayama"]
    ]
    for row in rows:
        ws.append(row)

    wb.save("example.xlsx")


if __name__ == "__main__":
    main()
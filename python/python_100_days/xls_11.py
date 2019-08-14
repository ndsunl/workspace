import openpyxl
from openpyxl.styles import Border, Side


def main():
    """
    设置单元格边框
    """
    wb = openpyxl.Workbook()
    ws = wb.active

    ws.title = "WorkSheetTitle"

    border = Border(
        left=Side(
            border_style="thin",
            color="FF0000"
        ),
        right=Side(
            border_style="thin",
            color="FF0000"
        ),
        top=Side(
            border_style="double",
            color="FF0000"
        ),
        bottom=Side(
            border_style="double",
            color="FF0000"
        )

    )

    b2 = ws["B2"]
    b2.border =border
    b2.value = "TEST"

    wb.save("example.xlsx")


if __name__ == "__main__":
    main()
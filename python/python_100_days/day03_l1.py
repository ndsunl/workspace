"""
英制单位与公制单位互换

Version: 0.1
Author: ndsunl
"""

value = float(input('请输入长度: '))
unit = input("请输入单位: ")
if unit == 'in' or unit == '英寸':
    print(f'{value:.2f}英寸 = {value * 2.54:.2f}厘米')
elif unit == 'cm' or unit == '厘米':
    print(f"{value:.2f}厘米 = {value / 2.54:.2f}英寸")
else:
    print("请输入有效的单位") 
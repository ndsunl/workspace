"""
将华氏温度转换为摄氏温度
F = 1.8C + 32

Version: 0.1
Author: ndsunl
"""

f = float(input('请输入华氏温度：'))
c = (f - 32) / 1.8
# 字符串格式化输出
print('%.1f华氏度 = %.1f摄氏度' % (f, c))
# 格式化字符串输出
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')
# 格式化函数输出
print("{:.1f}华氏度 = {:.1f}摄氏底".format(f, c))
"""
输入一个正整数判断它是不是素数

Version: 0.1
Author: ndsunl
Date: 2019-07-16
"""

from math import sqrt

num = int(input('请输入一个正整数: '))
end = int(sqrt(num))
print(end)
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print(f"{num} 是素数")
else:
    print(f"{num} 不是素数")

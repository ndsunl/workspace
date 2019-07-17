"""
寻找水仙花数，水仙花数是指一个 3 位数，它的每个位上的数字的 3 次幂之和等于它本身

Version: 0.1
Author: ndsunl
"""
import math

print("水仙花数： ", end="")
for i in range(100, 1000):
    a = i // 100
    b = i // 10 % 10
    c = i % 10
    if math.pow(a, 3) + math.pow(b, 3) + math.pow(c, 3) == i:
        print(i, end=' ')
print()
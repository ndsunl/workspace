"""
生成“斐波那契数列”
递推方法：F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=3，n∈N*）

Version: 0.1
Author: ndsunl
"""

print("斐波那契数列前 20 个数: ")
a = 0
b = 1
for _ in range(20):
    a, b = b, a + b
    print(a, end=" ")
print()


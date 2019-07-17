"""
寻找“完美数”，如果一个数恰好等于它的因子之和，则称该数为“完美数”

Version: 0.1
Author: ndsunl
"""

for i in range(2, 10000):
    sum = 0
    for j in range(1, i):
        if i % j == 0: 
            sum += j
    if sum == i:
        print(i)
"""
分段函数求值

       3x - 5  (x > 1)
f(x) = x + 2   (-1 <= x <= 1)
       5x + 3  (x <= -1)

Version: 0.1
Author: ndsunl
"""

x = float(input("x = "))
if x > 1:
    y = 3 * x - 5
elif x < -1:
    y = 5 * x + 3
else:
    y = x + 2
print(f"x({x:.2f}) = {y:.2f}")
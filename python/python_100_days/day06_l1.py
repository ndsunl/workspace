"""
实现计算求最大公约数和最小公倍数的函数

Version: 0.1
Author: ndsunl
"""


def gcd(x, y):
    """求最大公约数"""
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x, y):
    """求最小公倍数"""
    return x * y // gcd(x, y)


if __name__ == '__main__':
    x = int(input("x = "))
    y = int(input("y = "))
    print(f"{x} 和 {y} 的最大公约数是 {gcd(x, y)}")
    print(f"{x} 和 {y} 的最小公倍数是 {lcm(x, y)}")
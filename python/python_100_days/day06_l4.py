"""
判断输入的正整数是不是回文素数
"""

import day06_l2 as palindrome
import day06_l3 as prime

if __name__ == '__main__':
    num = int(input("请输入正整数: "))
    if palindrome.is_palindrome(num) and prime.is_prime(num):
        print(f"{num} 是回文素数")
    else:
        print(f"{num} 不是回文素数")
def is_palindrome(num):
    """判断一个数是否回文数"""
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num


if __name__ == '__main__':
    num = int(input("请输入一个整数: "))
    print(f"{num} 是回文数") if is_palindrome(num) else print(f"{num} 不是回文数")
def is_prime(num):
    """判断一个数是不是素数"""
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True if num != 1 else False
    

if __name__ == '__main__':
    num = int(input("请输入一个整数: "))
    print(f"{num} 是素数") if is_prime(num) else print(f"{num} 不是素数")
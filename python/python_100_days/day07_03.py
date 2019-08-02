def main():
    fruits = ['grape', 'apple', 'stawberry', 'waxverry']
    fruits += ['pitaya', 'pear', 'mango']
    # 循环遍历列表元素
    for fruit in fruits:
        print(fruit.title(), end=' ')
    print()
    # 列表切片
    fruits2 = fruits[1:4]
    print(fruits2)
    # fruits3 = fruits 没有复制列表只是创建了新的引用
    # 可以通过完整切片操作来复制列表
    fruits3 = fruits[:]
    print(fruits3)
    fruits4 = fruits[-3:-1]
    print(fruits4)
    # 反向切片
    fruits5 = fruits[::-1]
    print(fruits5)


if __name__ == '__main__':
    main()
def main():
    set1 = {1, 2, 3, 3, 3,2}
    print(set1)
    print('Lenght =', len(set1))
    set2 = set(range(1, 10))
    print(set2)
    set1.add(4)
    set1.add(5)
    set2.update([11, 12])
    print(set1)
    print(set2)
    set2.discard(5)
    # remove不存在的元素会引发KeyError
    if 4 in set2:
        set2.remove(4)
    print(set2)
    # 遍历集合
    set3 = set((1, 2, 3, 3, 2, 1))
    print(set3.pop())
    print(set3)
    # 集合交集、并集、差集、对称差运算
    print(set1 & set2)
    print(set1 | set2)
    print(set1 - set2)
    print(set1 ^ set2)
    # 判断子集和超集
    print(set2 <= set1)
    print(set3 <= set1)
    print(set1 >= set2)
    print(set1 >= set3)


if __name__ == '__main__':
    main()
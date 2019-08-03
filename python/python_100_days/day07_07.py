import sys


def main():
    # 定义元组
    t = ('骆昊', 38, True, '四川成都')
    print(t)
    # 获取元组中的元素
    print(t[0])
    print(t[3])
    # 遍历元组中的值
    for member in t:
        print(member)
    # 重新给元组赋值
    # 变量t重新引用了新的元组，原来的元组将被回收
    t = ("王大锤", 20, True, "云南昆明")
    print(sys.getsizeof(t))
    print(t)
    # 将元组转换成列表
    person = list(t)
    print(sys.getsizeof(person))
    print(person)
    # 修改列表元素
    person[0] = '李小龙'
    person[1] = 25
    print(person)
    # 将列表转换成元组
    fruits_list = ['apple', 'banana', 'orange']
    fruits_tuple = tuple(fruits_list)
    print(fruits_tuple)


if __name__ == '__main__':
    main()
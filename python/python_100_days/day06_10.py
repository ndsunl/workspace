def foo():
    global a
    a = 200
    print(a)    # 200


def main():
    foo()
    print(a)    # 200


if __name__ == '__main__':
    a = 100
    main()

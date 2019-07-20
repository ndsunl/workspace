def foo():
    a = 100

    def bar():
        nonlocal a
        a = 200
        print(a)    # 200

    bar()
    print(a)        # 200


def main():
    foo()


if __name__ == '__main__':
    main()

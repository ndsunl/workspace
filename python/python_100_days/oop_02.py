# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print(f"{self.__name}:{self.__score}")

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'


def main():
    bart = Student("Bart Simpson", 59)
    lisa = Student("Lisa Simpson", 99)
    bart.print_score()
    lisa.print_score()
    print(f"{bart.get_name()}:{bart.get_grade()}")
    # 访问私有变量可以变量名前加：_ClassName
    # 不建议如此使用
    print(f"{lisa._Student__name}:{lisa.get_grade()}")
    bart.set_score(76)
    print(f"{bart.get_name()}:{bart.get_grade()}")


if __name__ == "__main__":
    main()

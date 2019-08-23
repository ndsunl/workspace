class Student(object):

    # 初始化并绑定name和age属性
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def study(self, course_name):
        print(f"{self.name}正在学习{course_name}")


    def watch_movie(self):
        if self.age < 18:
            print(f'{self.name}只能观看熊出没')
        else:
            print(f"{self.name}正在观看好莱坞大片")


def main():
    # 创建对象并指定姓名和年龄    
    stu1 = Student('陈晓', 12)
    # 给对象发送study消息
    stu1.study('国际象棋')
    # 给对象发送watch_movie消息
    stu1.watch_movie()

    stu2 = Student('陈曦', 43)
    stu2.study('Python')
    stu2.watch_movie()


if __name__ == '__main__':
    main()
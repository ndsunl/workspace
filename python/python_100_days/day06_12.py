"""
作用域示例

Version: 0.1
Author: ndsunl
"""

v = 100     # 全局作用域
g = 100
print(f"全局变量.v = {v}")
print(f"全局变量.g = {g}")

def fun1():
    global g    # 声明后可对外部作用域的变量进行修改
    g = 200
    v = 200     # 外部嵌套函数作用域
    n = 200
    print(f"fun1.v = {v}")
    print(f"fun1.n = {n}")

    def fun2():
        nonlocal n  # 声明后可对外部嵌套函数作用域的变量进行修改
        n = 300
        v = 300     # 局部作用域
        print(f"fun2.v = {v}")
        print(f"fun2.n = {n}")
        print(max)  # max 函数都没有创建，在内建函数作用域中
                    # 只读，不可改变
                    # 可以在其余三个作用域重新创建

    fun2()
    print(f"fun1.n = {n}")

fun1()
print(f"全局变量.v = {v}")
print(f"全局变量.g = {g}")
print(max)  # max变量定义在内置模块的作用域
            # 是解释执行器提前定义好的
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""方法重写 override"""

# 定义父类
class Parent:
    def myMethod(self):
        print('调用父类方法')

# 定义子类
class Child(Parent):
    def myMethod(self):
        print('调用子类方法')

# 子类实例
c = Child()
# 子类调用重写方法
c.myMethod()
    

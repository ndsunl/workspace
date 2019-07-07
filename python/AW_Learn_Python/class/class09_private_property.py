#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""私有属性 private property"""

class JustCounter:
    __secretCount = 0   # 私有属性
    pulicCount =0       # 公开属性

    def count(self):
        self.__secretCount += 1
        self.pulicCount += 1
        print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print(counter.pulicCount)

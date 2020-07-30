#-*- coding:utf-8 -*-
import random

c = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(110000):
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    d = a + b
    c[d] += 1

for i in range(2, 13):
    print i, "出现", c[i], "次"
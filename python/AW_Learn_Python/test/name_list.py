#!/usr/bin/env python
# -*- coding: utf-8 -*-

names = ['sunny', 'snow', 'xiaoxiao']

for i in range(len(names)):
    print(names[i].title())

message = "How ary you?"
for i in names:
    print("%s, %s" % (i.title(), message))

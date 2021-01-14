#-*- coding:utf-8 -*-

import easygui
a = easygui.integerbox("请输入你的智商", upperbound=500)
while a != 250 and a != 0:
    easygui.msgbox ("you are not right! you are a pig!")
    a = easygui.integerbox("请输入你的智商")
if a == 250:
    easygui.msgbox ("你的智商是250")
else:
    easygui.msgbox("你的智商是0")

"""
用户身份验证

Version: 0.1
Author: ndsunl
"""
import getpass

username = input("请输入用户名: ")
# getpass 模块的 getpass 函数, 使输入口令时，终端中没有回显
password = getpass.getpass("请输入口令: ")
if username == "admin" and password == '123456':
    print('身份验证成功！')
else:
    print('身份验证失败！')
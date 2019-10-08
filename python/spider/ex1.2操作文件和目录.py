import os

# 当前工作目录
print(f"当前Python脚本工作目录: {os.getcwd()}")

# 创建空文件
f = open('readme', 'w')
f.close
# 列目录
print(f"列目录: {os.listdir(os.getcwd())}")
# 移除文件
os.remove("readme")
print(f"列目录: {os.listdir(os.getcwd())}")

# 创建空目录
os.mkdir("temp")
print(f"列目录: {os.listdir(os.getcwd())}")
# 移除空目录
os.removedirs("temp")
print(f"列目录: {os.listdir(os.getcwd())}")
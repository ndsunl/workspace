'''
文件读写
'''

# 读取
f = open(r'/home/jackchen/missfont.log', 'r')
print(f.read())
f.close()

# try ... finally 保证程序健壮性
try:
    f = open(r'/home/jackchen/missfont.log', 'r')
    print(f.read())
finally:
    if f:
        f.close()

# with 代替 try ... finally
with open(r'/home/jackchen/missfont.log', 'r') as fileReader:
    print(fileReader.read())

# 每次读取一行
with open(r'/home/jackchen/missfont.log', 'r') as fileReader:
    for line in fileReader.readlines():
        print(line.strip())

# 写入文件
f = open(r'/home/jackchen/missfont.log', 'w')
f.write('Hello python!')
f.close()

# with ... as
with open(r'/home/jackchen/missfont.log', 'a') as fileWriter:
    fileWriter.write('Hello world!')
    fileWriter.close()

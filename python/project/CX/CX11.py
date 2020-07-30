#-*- coding:utf-8 -*-

numBlocks = int(raw_input("请输入星号的数量："))
for block in range(1, numBlocks + 1):
    print 'block:' + str(block)
    for line in range(1, block * 2):
        print 'line:' + str(line)
        for star in range(1, (block + line) * 2):
            print 'star:' + str(star),
            print '*',     
        print
    print    
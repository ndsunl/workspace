# ！/usr/bin/env python3
# -*-coding: UTF-8 -*-

# =================================
# funtion: 批量下载 youku 播单视频
# Author ndsunl
# =================================

import os


def get_format(url):
    """获取优酷视频最高的格式标志
    """
    pass


def get_url(filepath):
    """遍历文件夹下所有文件并取得播单名及视频下载地址
    param:
        filepath: 要遍历的目录名

    return:
        data: [[文件名，url1, url2, ...], [...], ...]
    """
    files = os.listdir(filepath)    # 获取目录下所有文件名
    data = []

    # 遍历文件夹
    for file in files:
        s = []
        if not os.path.isdir(file): # 判断是否文件夹，不是文件夹才打开
            s.append(file.strip('.txt'))
            f = open(filepath + '/' + file) # 打开文件
            iter_f = iter(f)    # 创建迭代器
            for line in iter_f:
                s.append(line.strip('\n'))
            data.append(s)
    
    return data


def get_vedio(url, vedio_format):
    """批量下载播单视频
    """
    pass


def main():
    filepath = input('请输入文件路径：')
    url = get_url(filepath)
    for i in range(len(url)):
        print("===========================================")
        for j in range(len(url[i])):
            print(url[i][j])
    
    #vedio_format = get_format(url)
    #get_vedio(url, vedio_format)


if __name__ == "__main__":
    main()

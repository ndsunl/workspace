# ！/usr/bin/env python3
# -*-coding: UTF-8 -*-

# =================================
# funtion: 批量下载 youku 播单视频
# Author ndsunl
# =================================

import os
import time
import re


def get_format(url):
    """获取优酷最高分辨率视频的格式标志
    """
    s = 60
    i = 2
    readobj = os.popen(f'you-get -i {url}')
    info = readobj.read()
    readobj.close()
    while info == "":
        print(f'error: {info} 获取数据错误，{i}分钟后再次获取数据')
        time.sleep(s*i)
        readobj = os.popen(f'you-get -i {url}')
        info = readobj.read()
        readobj.close()
        i+=2
    format = []
    size = []
    # 提取数据
    for line in info.splitlines():  # 按行分割字符串
        if re.search(r'format:', line) is not None:
            temp = re.search(r'7m\w*', line).group()
            temp = re.sub(r'7m', '', temp)
            format.append(temp) 
        if re.search(r'size:', line) is not None:
            temp = re.search(r'size:\s*\d*\.\d*', line).group()
            temp = re.sub(r'size:\s*', '', temp)
            size.append(temp) 
    format_dict = dict(zip(format, size))
    format_list = sorted(format_dict.items(), key=lambda item:item[1], reverse=True)

    return format_list[0][0]


def get_url(filepath):
    """遍历文件夹下所有文件并取得播单名及视频下载地址
    param:
        filepath: 要遍历的目录名

    return:
        返回值 data 为字典
        键名为文件名，即播单名；值为列表，其内容为该播单所有的视频下载地址
        
        data: {文件名:[url1, url2, ...], ...}
    """
    files = os.listdir(filepath)    # 获取目录下所有文件名
    data = {}

    for file in files:  # 遍历文件夹
        values = []
        if not os.path.isdir(file): # 判断是否文件夹，不是文件夹才打开
            bd = file.strip('.txt')
            f = open(filepath + '/' + file) # 打开文件
            iter_f = iter(f)    # 创建迭代器
            for line in iter_f: # 遍历文件
                values.append(line.strip('\n'))   
        data[bd] = values
    
    return data


def get_vedio(urls):
    """批量下载播单视频
    """
    # 取播单名，并创建文件夹
    for key, value in urls.items():
        path = os.getcwd() + '/download/' + key
        if not os.path.exists(path):
            os.makedirs(path)
        #path = os.getcwd()+ '/download/' + key
 
        print('=====================================')
        print(f"正在下载播单：{key}，共 {len(value)} 个视频，请稍候 ...")
        for i in range(len(value)):
            if i == 0:
                format = get_format(value[i])
            print(f'此播单分辨率最高的视频格式是{format}')
            info = os.system(f"you-get -F {format} -o {path} {value[i]}")
            print(f"you-get -F {format} -o {path} {value[i]}")
            count = 2
            s = 60
            while info !=0:
                print(f'下载出错，错误码{info}。{count}分钟后再次下载，请稍候 ...')
                time.sleep(s*count)
                count+=2
                info = os.system(f"you-get -F {format} -o {path} {value[i]}")

                
            #print(f"  第 {each} ")
            #info = os.system(f"you-get -o {path} {each}")
     

def main():
    filepath = input('请输入文件路径：')
    urls = get_url(filepath)
    #for key, value in url.items():
    #    print("===========================================")
    #    print(key)
    #    for each in value:
    #        print(each)
    
    get_vedio(urls)


if __name__ == "__main__":
    main()

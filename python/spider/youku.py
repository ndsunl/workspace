import requests
from bs4 import BeautifulSoup
import re
import os


def open_url(url):
    """ 抓取指定网页
    
    param: 
        url: 要抓取的网址
    
    return: 
        即要抓取的网页内容，Response 对象
    """
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
    res = requests.get(url, headers=headers)

    return res


def get_url(url):
    """ 获取播单下所有视频播放地址
    
    param:
        url: 播单地址或单个视频地址
    
    return:
        列表 data 为播单下所有视频播放地址
    """
    data = []
    str = 'http://player.youku.com/embed/'

    while data == []:
        res = open_url(url)
        soup = BeautifulSoup(res.text, 'html.parser')

        bz = re.search(r'albumlist\/show\/id_', url)
        if bz is None:  # 单个视频
            class_a = 'anthology-content'
            class_b = 'pic-text-item'
        else:           # 播单
            class_a = 'fix'
            class_b = 'p-thumb'

        target = soup.find('div', class_=class_a)
        
        if target != None:
            target = target.find_all('div', class_=class_b)
            # 解析并将播单下所有视频播放地址加入列表
            for i in range(len(target)):
                url = target[i].a.get('href')
                url = re.search(r'\/\/v\.youku\.com\/v_show\/id_\w*', url).group()
                url = re.sub(r'\/\/v\.youku\.com\/v_show\/id_', str, url)
                data.append(url)
        else:
            print(f'播单页面获取出错，正在重新抓取数据 ... ')

    return data


def get_channel(res):
    """ 解析并提取自频道中播单地址及播单名
    
    param:
        res: 要解析的网页内容，Response 对象
    
    return:
        返回值 data 为包含播单地址及播单名的列表
        example: [{'url': 播单地址, 'title': 播单名}, {...}]
    """
    data = []
    soup = BeautifulSoup(res.text, 'html.parser')
    target = soup.find_all('div', class_='album-cover')

    for i in range(len(target)):
        # 获取播单名, 同时删除播单名中的中文符号
        title = target[i].a.get('title')
        title = re.sub(r'[〈〉-《》【】-]', '_', title)
        title = re.sub(r'^_|_$', '', title)
        title = re.sub(r'__', '_', title)
        
        # 获取有效播单地址
        channel_url = 'http:' + target[i].a.get('href')
        item = target[i].parent
        v_link = item.find_all('div', class_='v-link')
 
        for i in range(len(v_link)):
            list_url = 'http:' + v_link[i].a.get('href')
            list_title = v_link[i].a.get('title')
            if list_title != '[此视频无法播放]' and re.search('v\.youku\.com', list_url) is not None:
                channel_url = list_url
                break
        data.append({'url':channel_url, 'title':title})

    return data


def save_url(data, title):
    """ 将视频播放地址存入指定文件

    param：
        data: 包含播单中所有视频播放地址的列表
        title: 播单名
    """
    if len(data) != 0:
        if not os.path.exists('vedio'):
            os.makedirs('vedio')

        filename = 'vedio/' + title + '.txt'
        with open(filename, 'w', encoding='utf-8') as f:
            for i in range(len(data)):
                f.write(data[i] + '\n')
        f.close
        print(f'视频播放地址已存入文件：{filename}')


def get_page(res):
    """ 获取播单页数

    param:
        res: 要解析的网页内容，Response 对象
    
    return:
        播单页数
    """
    soup = BeautifulSoup(res.text, 'html.parser')
    if soup.find('li', class_='next').previous_sibling.a != None:
        page = soup.find('li', class_='next').previous_sibling.a.text
    else:
        page = soup.find('li', class_='next').previous_sibling.span.text

    return int(page)


def main():
    channel_data = []
    print('优酷自频道播单视频下载地址爬取工具\n')
    url = input("请输入优酷自频道\自频道播单地址:")

    # 检查是否优酷地址    
    while re.search(r'i\.youku\.com\/', url) is None:
        print('\nerror: 您输入的不是优酷自频道或自频道播单地址！请重新输入')
        url = input("请输入优酷地址:")

    # 自频道地址转为播单列表地址
    if re.search(r'playlists', url) is None and re.search(r'\/i\.youku\.com\/i', url) is not None:
        url = url + '/playlists?spm=a2hzp.8244740.0.0'
        
    res = open_url(url) 
    page = get_page(res)
    # 获取当页所有播单地址
    for i in range(page):
        print("")
        print(f"===================== 正在抓取播单第 {i+1} 页 =====================")
     
        channel_url = url + '&order=1&page=' + str(i+1)
        res = open_url(channel_url)
        channel_data = get_channel(res)

        # 获取播单所有视频下载地址并存盘
        for j in range(len(channel_data)):
            channel_url = channel_data[j].get('url')
            channel_title = str(i) + str(j) + '_' +channel_data[j].get('title')
            vedio_data = get_url(channel_url)
            save_url(vedio_data, channel_title)


if __name__ == "__main__":
    main()
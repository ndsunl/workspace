#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   必应壁纸下载榜.py
@Time    :   2020/12/12 20:04:16
@Author  :   ndsunl
@Desc    :   爬取必应壁纸下载榜中的壁纸
'''

import requests
import bs4
import re

'''
功能：获取页面
参数：num = 要获取的页数
'''
def get_page(num):
    page_list = []
    url = "https://bing.ioliu.cn/ranking?p="
    for i in range(1, num+1):
        page_list.append(f"{url}{i}")
    return page_list

def get_html(url):
    header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
    res = requests.get(url, header=header)
    html = res.text
    return html

def parse_html(html):
    soup = bs4.BeautifulSoup(html, "html.parser")
    url = soup.find_all('data-progressive', )
    pass

def download():
    pass

def main()
    pass

if __name__ == "__main__":
    main()
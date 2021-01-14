#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   豆瓣电影TOP250.py
@Time    :   2020/12/12 10:56:40
@Author  :   ndsunl
@Desc    :   爬取豆瓣电影TOP250列表，并保存至 movies.txt 中。
'''

import requests
import bs4


def get_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
    res = requests.get(url, headers=headers)

    return res


def get_page(res):
    """获取页数"""
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    page = soup.find('span', class_='next').previous_sibling.previous_sibling.text
    
    return int(page)

def get_movies(res):
    """获取电影信息"""
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    
    # 电影名称
    title = []
    targets = soup.find_all('div', class_='hd')
    for each in targets:
        title.append(each.a.span.text)

    # 电影评分
    rating = []
    targets = soup.find_all('span', class_='rating_num')
    for each in targets:
        rating.append(f' 评分：{each.text} ')

    # 电影详情
    detail = []
    targets = soup.find_all('div', class_='bd')
    for each in targets:
        try:
            detail.append(each.p.text.split('\n')[1].strip()+each.p.text.split('\n')[2].strip())
        except:
            continue

    # 信息组合
    result = []
    lenght = len(title)
    for i in range(lenght):
        result.append(title[i] + rating[i] + detail[i] + '\n')

    return result


def main():
    host = 'https://movie.douban.com/top250'
    res = get_url(host)
    page = get_page(res)

    result = []
    for i in range(page):
        url = f'{host}?start={25*i}'
        res = get_url(url)
        result.extend(get_movies(res))

    with open('spider/movies.txt', 'w', encoding='utf-8') as f:
        for each in result:
            f.write(each)
        f.close()


if __name__ == "__main__":
    main()
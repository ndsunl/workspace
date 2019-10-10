import requests
import bs4
import re


def open_url(url):
    # 使用代理
    # proxies = {"http":"127.0.0.1:1080", "https":"127.0.0.1:1080"}
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'}
    # res = requests.get(url, headers=headers, proxies=proxies)
    res = requests.get(url, headers=headers)

    return res

def find_movies(res):
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # 电影名
    movies = []
    targets = soup.find_all('div', class_="hd")
    


res = requests.get("https://movie.douban.com/top250")
soup = bs4.BeautifulSoup(res.text, "html.parser")
targets = soup.find_all('div', class_="hd")
for each in targets:
    print(each.a.span.text)

import requests
import bs4
import re


def open_url(url):
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
    res = requests.get(url, headers=headers)

    return res


def main():
    url = "http://list.youku.com/albumlist/show/id_21619857"
    res = open_url(url)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    with open('youku.txt', 'w', encoding='utf-8') as f:
        for each in soup:
            f.write(each)
        f.close


if __name__ == "__main__":
    main()

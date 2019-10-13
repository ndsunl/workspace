import requests
import bs4


def get_url(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
    res = requests.get(url, headers=headers)

    return res


def get_title(res):
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    title = soup.find('h1', class_='post-title').a.text.strip()

    return title


def main():
    url = "http://www.santostang.com/"
    res = get_url(url)
    title = get_title(res)
    print(title)

    with open('title.txt', 'a+', encoding='utf-8') as f:
        f.write(title)


if __name__ == "__main__":
    main()

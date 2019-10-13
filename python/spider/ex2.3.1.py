import requests


def get_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
    res = requests.get(url, headers=headers)

    return res


def main():
    url = 'http://www.santostang.com/'
    res = get_url(url)

    with open('santostang.txt', 'w', encoding='utf-8') as f:
        f.write(res.text)
        f.close


if __name__ == "__main__":
    main()

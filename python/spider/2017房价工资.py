import requests, bs4, re


def open_url(url):
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
    res = requests.get(url, headers=headers)

    return res


def find_data(res):
    data = []
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    target = soup.find_all('p', style="TEXT-INDENT: 2em")
    target = iter(target)

    for each in target:
        if each.text.isnumeric():
            data.append([
                re.search(r'\[(.+)\]',next(target).text).group(1),
                next(target).text,
                next(target).text,
                next(target).text])

    return data


def main():
    url = "https://news.house.qq.com/a/20170702/003985.htm"
    res = open_url(url)
    print(find_data(res))


if __name__ == "__main__":
    main()

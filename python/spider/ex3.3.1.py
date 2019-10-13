import requests


def get_url(url):
    key_dict = {'key1': 'value1', 'key2': 'value2'}
    res = requests.get(url, params=key_dict)

    return res


def main():
    url = 'http://httpbin.org/get'
    res = get_url(url)

    print('URL 已正确编码：', res.url)
    print('字符串方式的响应体：\n', res.text)


if __name__ == "__main__":
    main()

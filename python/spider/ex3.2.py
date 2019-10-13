import requests


def main():
    r = requests.get('http://www.santostang.com/')
    print('文本编码：', r.encoding)
    print('响应状态码：', r.status_code)
    print('字符串方式的响应体：', r.text)


if __name__ == "__main__":
    main()

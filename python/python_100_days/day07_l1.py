import os
import time


def main():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清屏
        os.system('clear')
        print(content)
        # 休眠 200 毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()
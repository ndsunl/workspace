import requests
import bs4


def get_url(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
    res = requests.get(url, headers=headers)

    params = 'OIFN8Rfs9xePiJaUFDt9DMbFT1wNADW0IoEFP2UMyc9ErwuOE/SJPxx/BF/46ttGd3UyYe6X7IhnfixKazKWucIkQSoeXOESBPxXnGHjS5HMqZVbWPybIF4cbZg8ItVog84oCTSZIxCJ/H2U0YH4/sxk81bHuRn556+31rVoujk6YgCajHtiUhlpNA1iRfvL'
    encSecKey = '7d65cbc8b75413deeffdd086dd4f85300f80846ec82314ad4d87302a2d35f4e2c5fb8cf917f1dd687edd0dc3b8bbe18370cb8c99ee10f0f65ad72ddbfcec0e2c01cae6bbba624da189ebea430f20b19e3796577de86355c379c05b96c43149f04349a4302d23bf2817857e609c8eb455a2627fc7a3b2be13731b73f396cd9429'
    data = {
        'params': params,
        'encSecKey': encSecKey}
    target_url = 'https://music.163.com/weapi/v1/resource/comments/R_SO_4_4466775?csrf_token='

    res = requests.post(target_url, headers=headers, data=data)
    
    return res



def main():
    url = input('请输入链接地址：')
    res = get_url(url)

    with reac

if __name__ == "__main__":
    main()

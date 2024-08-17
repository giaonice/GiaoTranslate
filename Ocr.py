# -*- coding:utf-8 -*-
import random
import re
import string
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

def Ocr():
    try:
        headers = {
            'referer': 'https://uutool.cn/ocr/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        }
        response = requests.get('https://uutool.cn/ocr/', headers = headers)
        token = re.findall("token = '(.*?)'", response.text, re.S)[0]
        print('token', token)
        boundary = '----WebKitFormBoundary' + ''.join(random.sample(string.ascii_letters + string.digits, 16))
        headers = {
            'content-type': f'multipart/form-data; boundary={boundary}',
            'origin': 'https://uutool.cn',
            'referer': 'https://uutool.cn/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        }
        field = {
            'token': token,
            'file': ('img.png', open('img.png', "rb"), 'image/jpeg')
        }
        data = MultipartEncoder(fields = field, boundary = boundary)

        response = requests.post('https://api.uutool.cn/photo/ocr/', headers = headers, data = data).json()
        str_ = ''
        print(response)
        for i in range(0, response["data"]['count']):
            if i != 0:
                str_ += '    ' + response["data"]['rows'][i]
            else:
                str_ = response["data"]['rows'][i]
        return str_
    except:
        return '网路错误  or  接口返回数据错误！！！'


if __name__ == '__main__':

    print(Ocr())

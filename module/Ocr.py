# -*- coding:utf-8 -*-
import random
import re
import string
import requests
from PyQt5.QtCore import pyqtSignal, QThread
from requests_toolbelt.multipart.encoder import MultipartEncoder

class Ocr(QThread):
    dataProcessed = pyqtSignal(str)  # 更有描述性的信号名

    def __init__(self, parent = None):
        super().__init__(parent)

    def run(self):
        try:
            headers = {
                'referer': 'https://uutool.cn/ocr/',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                              '(KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
            }
            response = requests.get('https://uutool.cn/ocr/', headers = headers)
            token = re.findall("token = '(.*?)'", response.text, re.S)[0]
            print('token', token)
            boundary = '----WebKitFormBoundary' + ''.join(random.sample(string.ascii_letters + string.digits, 16))
            headers = {
                'content-type': f'multipart/form-data; boundary={boundary}',
                'origin': 'https://uutool.cn',
                'referer': 'https://uutool.cn/',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                              '(KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
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
            print(str_)
            self.dataProcessed.emit(str_)
        except:
            self.dataProcessed.emit('网路错误  or  接口返回数据错误！！！')


if __name__ == '__main__':

    print(Ocr())

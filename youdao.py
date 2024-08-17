# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
import json
import time
import requests
import base64
import hashlib
from Crypto.Cipher import AES  # pip install pycryptodome
from Crypto.Util.Padding import unpad


class Translate(object):
    def __init__(self, word):
        self.word = word
        self.sign = ''
        self.response = ''
        self.get_sign()

    def get_result(self):
        try:
            self.get_response()
            result = json.loads(self.encrypt_data())
            if result['code'] == 0 and 'dictResult' in result.keys() and result['type'] == 'en2zh-CHS':
                temp = result["dictResult"]["ec"]['word']
                str_ = ''
                for i in temp['trs']:
                    str_ += f"✨  {i['pos']}  {i['tran']}\n"
                return {
                    'code': 0,
                    'result': str_,
                    'src': result['translateResult'][0][0]['src'],
                    'type': result['type']
                }
            elif result['code'] == 0:
                return {
                    'code': 0,
                    'result': result['translateResult'][0][0]['tgt'],
                    'src': result['translateResult'][0][0]['src'],
                    'type': result['type']
                }
            else:
                return {
                    'code': 1,
                    'result': '接口返回数据错误！！！'
                }
        except:
            return {
                'code': 1,
                'result': '网路错误  or  接口返回数据错误！！！'
            }

    # 获取sign
    def get_sign(self):
        timestamp = int(time.time() * 1000)
        e = f'client=fanyideskweb&mysticTime={timestamp}&product=webfanyi&key=fsdsogkndfokasodnaso'
        self.sign = hashlib.md5(e.encode()).hexdigest()

    # 获取数据
    def get_response(self):
        headers = {
            'Cookie': 'OUTFOX_SEARCH_USER_ID_NCOO=1948382659.381789; OUTFOX_SEARCH_USER_ID=1775497575@183.219.26.105; __yadk_uid=5QwMgTGcByPM5Fdhip58d5m1lBPBpGCW; rollNum=true; ___rl__test__cookies=1708157820132',
            'Referer': 'https://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        }
        data = {
            'i': self.word,
            'from': 'auto',
            'to': '',
            'domain': '0',
            'dictResult': 'true',
            'keyid': 'webfanyi',
            'sign': self.sign,
            'client': 'fanyideskweb',
            'product': 'webfanyi',
            'appVersion': '1.0.0',
            'vendor': 'web',
            'pointParam': 'client,mysticTime,product',
            'mysticTime': str(int(time.time() * 1000)),
            'keyfrom': 'fanyi.web',
            'mid': '1',
            'screen': '1',
            'model': '1',
            'network': 'wifi',
            'abtest': '0',
            'yduuid': 'abcdefg',
        }
        self.response = requests.post('https://dict.youdao.com/webtranslate', headers = headers, data = data).text

    # 数据解密
    def encrypt_data(self):
        # 先把密匙和偏移量进行md5加密 digest()是返回二进制的值
        key = hashlib.md5("ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl".encode()).digest()
        iv = hashlib.md5("ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4".encode()).digest()
        cipher = AES.new(key, AES.MODE_CBC, iv)  # 创建一个AES对象（密钥，模式，偏移量）
        ciphertext = base64.urlsafe_b64decode(self.response)  # 解码为原始的字节串
        plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
        return plaintext.decode()


if __name__ == '__main__':
    t = Translate('elite')
    print(t.get_result())
    t = Translate("This library uses 'blocking' socket I/O. If you are looking for a library with 'non-blocking' socket I/O, this is not the one that you want.")
    print(t.get_result())

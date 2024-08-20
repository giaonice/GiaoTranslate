import random
import time
import requests
import hashlib


class Translate(object):
    def __init__(self, word):
        self.word = word
        self.data_1 = "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                      "Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30"

    def get_result(self):
        try:
            md5 = hashlib.md5()
            md5.update(self.data_1.encode())
            bv = md5.hexdigest()
            ts = str(int(time.time()*1000))
            salt = ts + str(random.randint(1, 10))
            sign = hashlib.md5(("fanyideskweb" + self.word + salt + "Y2FYu%TNSbMCxc3t2u^XT").encode()).hexdigest()
            data = {
                'i': self.word,
                'from': 'AUTO',
                'to': 'AUTO',
                'smartresult': 'dict',
                'client': 'fanyideskweb',
                'salt': salt,
                'sign': sign,
                'lts': ts,
                'bv': bv,
                'doctype': 'json',
                'version': '2.1',
                'keyfrom': "fanyi.web",
                'action': "FY_BY_REALTlME",
            }
            url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
            headers = {
                "Cookie": 'OUTFOX_SEARCH_USER_ID=-70076830@10.169.0.81; JSESSIONID=aaaBgySEBI8iqap1h-A6x; '
                          'OUTFOX_SEARCH_USER_ID_NCOO=1426669139.1908152; ___rl__test__cookies=1643277756230',
                "Referer": "https://fanyi.youdao.com/",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/74.0.3729.169 Safari/537.36",
            }
            result = requests.post(url = url, headers = headers, data = data).json()
            if result['errorCode'] == 0:
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

class Trsnalation2(object):
    def __init__(self, word):
        self.word = word

    def generatesaltsign(self):
        navigator_appversion = "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                          "Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30"
        t = hashlib.md5(navigator_appversion.encode()).hexdigest()
        r = str(int(time.time() * 1000))
        i = r + str(random.randint(1, 10))
        return {
            "ts": r,
            "bv": t,
            "salt": i,
            "sign": hashlib.md5(str("fanyideskweb" + self.word + i + "Y2FYu%TNSbMCxc3t2u^XT").encode()).hexdigest()
        }


    def spider(self):
        url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        r = self.generatesaltsign()
        data = {
            "i": self.word,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": r["salt"],
            "sign": r["sign"],
            "ts": r["ts"],
            "bv": r["bv"],
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME",
        }
        headers = {
            "Cookie": 'OUTFOX_SEARCH_USER_ID=-70076830@10.169.0.81; JSESSIONID=aaaBgySEBI8iqap1h-A6x; '
                      'OUTFOX_SEARCH_USER_ID_NCOO=1426669139.1908152; ___rl__test__cookies=1643277756230',
            "Referer": "https://fanyi.youdao.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/74.0.3729.169 Safari/537.36",
        }
        response = requests.post(url = url, data = data, headers = headers)
        print(response.text)

if __name__ == '__main__':
    t = Translate('elite')
    t.get_result()
    t2 = Trsnalation2('result')
    t2.spider()

#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time         :       2021/8/31 9:47
# @Author       :       林子然
# @File         :       有道翻译纯Python解密.py
# @Software     :       Pycharm

from execjs import compile as cp
import requests

lang = {'中文 » 英语': ['zh-CHS', 'en'], '英语 » 中文': ['en', 'zh-CHS'], '中文 » 日语': ['zh-CHS', 'ja'], '日语 » 中文': ['ja', 'zh-CHS'], '中文 » 韩语': ['zh-CHS', 'ko'], '韩语 » 中文': ['ko', 'zh-CHS'], '中文 » 法语': ['zh-CHS', 'fr'], '法语 » 中文': ['fr', 'zh-CHS'], '中文 » 德语': ['zh-CHS', 'de'], '德语 » 中文': ['de', 'zh-CHS'], '中文 » 俄语': ['zh-CHS', 'ru'], '俄语 » 中文': ['ru', 'zh-CHS'], '中文 » 西班牙语': ['zh-CHS', 'es'], '西班牙语 » 中文': ['es', 'zh-CHS'], '中文 » 葡萄牙语': ['zh-CHS', 'pt'], '葡萄牙语 » 中文': ['pt', 'zh-CHS'], '中文 » 意大利语': ['zh-CHS', 'it'], '意大利语 » 中文': ['it', 'zh-CHS'], '中文 » 越南语': ['zh-CHS', 'vi'], '越南语 » 中文': ['vi', 'zh-CHS'], '中文 » 印尼语': ['zh-CHS', 'id'], '印尼语 » 中文': ['id', 'zh-CHS'], '中文 » 阿拉伯语': ['zh-CHS', 'ar'], '阿拉伯语 » 中文': ['ar', 'zh-CHS'], '中文 » 荷兰语': ['zh-CHS', 'nl'], '荷兰语 » 中文': ['nl', 'zh-CHS'], '中文 » 泰语': ['zh-CHS', 'th'], '泰语 » 中文': ['th', 'zh-CHS']}
with open('../有道翻译/有道翻译js解密.js', 'r', encoding='utf-8') as f:
    compile_result = cp(f.read())




headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'Cookie': 'OUTFOX_SEARCH_USER_ID=-1178965908@10.108.160.101; OUTFOX_SEARCH_USER_ID_NCOO=71209729.09664452; JSESSIONID=aaaIiP9foQs_J6G20BmYx; ___rl__test__cookies=1634443700702',
    'Host': 'fanyi.youdao.com',
    'Origin': 'https://fanyi.youdao.com',
    'Referer': 'https://fanyi.youdao.com/',
}
url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'


def translate(lang_from, lang_to, word):
    key = '%s » %s' % (lang_from, lang_to)
    value = lang[key]
    # print(value)
    result = compile_result.call('youdao', word)
    data = {
        'i': word,
        'from': value[0],
        'to': value[1],
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME',
    }
    data.update(result)
    response = requests.post(url, data=data, headers=headers)


    return response.json()['translateResult'][0][0]['tgt']


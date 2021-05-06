#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/8 20:38
# @Author  : h5osir
# @Email   : h5osir@outlook.com
# @Github  : https://github.com/H5oSir
# @Blog    : https://blog.csdn.net/Boy_Z
# @File    : chinazApi.py
# @Software: PyCharm
import requests
from lxml import etree
print(123456)
chinaz_url="http://tool.chinaz.com/subdomain/taobao.com"
headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        }
r = requests.get(url=chinaz_url,headers=headers)
print(r.status_code)
print(r.text)

# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    Filename:   RealTrafficIndex.py
    Author:     Helyao
    Description:
        Get real-time navinfo traffic index.
-------------------------------------------------
    http://www.nitrafficindex.com/
-------------------------------------------------
    Change Logs:
    2017-06-18  10:43pm     create
-------------------------------------------------
"""

import os
import time
import ujson
import requests
import datetime
import threading

URL = 'http://www.nitrafficindex.com/traffic/getRoadIndex.do'
DATA = 'areaCode=310000&roadLevel=1%2C3%2C4&page=1&rows=50'
# DATA = 'areaCode=110000&roadLevel=1%2C3%2C4'
HEADER = {
    'Pragma': "no-cache",
    "Referer": "http://www.nitrafficindex.com/trafficIndexAnalysis.html",
    'Content-Type': "application/x-www-form-urlencoded",
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",
    'Accept': "application/json, text/javascript, */*",
    'Connection': "keep-alive",
    'Origin': "http://www.nitrafficindex.com",
    'Cache-Control': "no-cache",
    'X-Requested-With': "XMLHttpRequest",
    'Accept-Encoding': "gzip, deflate",
    'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4'
}

response = requests.request('POST', URL, data=DATA, headers=HEADER, timeout=10, verify=False)
print(response.status_code)
results = ujson.decode(response.text)
print(results)
print(results['date'])
print(results['total'])
for item in results['rows']:
    print(item)

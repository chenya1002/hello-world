# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 20:03:57 2018

@author: chenya
"""
a=b'1'
print(a)
import urllib.request as r
data=r.urlopen('http://api.openweathermap.org/data/2.5/weather?q=shanghai&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996').read().decode('utf-8','ignore')
import json
data=json.loads(data)
print(data['main']['temp'])
print(data['weather'][0]['description'])
print(data['main']['pressure'])
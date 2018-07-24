# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 20:15:17 2018

@author: chenya
"""
import urllib.request as r
data=r.urlopen('http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric').read().decode('utf-8','ignore')

import json
data=json.loads(data)


print(data['list'][2]['main']['temp'])
print(data['list'][2]['main']['temp_min'])
print(data['list'][2]['main']['temp_max'])
print(data['list'][2]['weather'][0]['main'])

print(data['list'][10]['main']['temp'])
print(data['list'][10]['main']['temp_min'])
print(data['list'][10]['main']['temp_max'])
print(data['list'][10]['weather'][0]['main'])

print(data['list'][18]['main']['temp'])
print(data['list'][18]['main']['temp_min'])
print(data['list'][18]['main']['temp_max'])
print(data['list'][18]['weather'][0]['main'])

print(data['list'][26]['main']['temp'])
print(data['list'][26]['main']['temp_min'])
print(data['list'][26]['main']['temp_max'])
print(data['list'][26]['weather'][0]['main'])

print(data['list'][34]['main']['temp'])
print(data['list'][34]['main']['temp_min'])
print(data['list'][34]['main']['temp_max'])
print(data['list'][34]['weather'][0]['main'])

city=input('please enter the name of the city you want to query')
import urllib.request as r
url='http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url.format(city)).read().decode('utf-8','ignore')

import json
data=json.loads(data)
main=data['list'][0]['weather'][0]['main']
print('the weather is the case:'+main)


print('第一天tmp:'+'x'*int(data['list'][2]['main']['temp']))
print('第二天tmp:'+'x'*int(data['list'][10]['main']['temp']))
print('第二天tmp:'+'x'*int(data['list'][18]['main']['temp']))
print('第二天tmp:'+'x'*int(data['list'][26]['main']['temp']))
print('第二天tmp:'+'x'*int(data['list'][34]['main']['temp']))

z=data['list'][2]['main']['temp']
x=data['list'][10]['main']['temp']
c=data['list'][18]['main']['temp']
v=data['list'][26]['main']['temp']
b=data['list'][34]['main']['temp']
print('从小到大排序为：')
print(sorted([z,x,c,v,b]))





    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
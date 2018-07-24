# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 09:00:26 2018
########
练习题7：
1.使用多选其一完成天气的提醒，
淘宝客户端
2.一定要多次使用for循环，偶尔使用while循环
3.使用到break或continue,在淘宝客户端中
    

@author: chenya
"""
import urllib.request as r
data=r.urlopen('http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric').read().decode('utf-8','ignore')

import json
data=json.loads(data)

def mention():
    for i in range(2,36,8):
        print('第{}天'.format(i//8+1)+':')
        print('天气'+str(data['list'][i]['weather'][0]['description']))
        print('温度'+str(data['list'][i]['main']['temp']))
        if data['list'][i]['main']['temp']>30:
            print('气温较高，注意防晒！')
        elif data['list'][i]['main']['temp']>20:
            print('气温适中，适宜出行！')
        else:
            print('天气较冷，注意添加新衣！')
mention()

    
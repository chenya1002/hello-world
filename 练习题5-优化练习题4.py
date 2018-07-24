# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 09:35:54 2018

练习题5：
1.优化代码 用函数的方法修改练习四 输出每一天的天气函数
2.打印温度折线图，使用函数来优化（必须要有返回值）

函数（做某件事的指令的集合）：
变量（生命周期）
函数的语法1：
def 函数名():
    指令集合
函数的语法2（有参数的函数）：
def 函数名a,b,c,e():
    指令集合(a)
    指令集合(b,c,e)
函数语法3（函数的返回值=结果）：
def 函数名a,b,c,e():
    指令集合(a)
    指令集合(b,c,e)
    return xxx
@author: chenya
"""
a=3#全局变量，生命作用于整个环境
def calc():
    b=4#局部变量，内部变量，生命在缩进里面
    print(b)
calc()
print(b)
'''
函数的参数说明 鼠标在参数内+快捷键 ctrl i
'''
#函数语法2
def calc(a,b):
    #计算两个数之和
    print('a和b相加是：'+str(a+b))
calc(3,4)
print(calc(3,4))#没有返回值的函数
#calc('a','b')

#函数语法3
def calc(a,b,c):
    return a+b+c
print(calc(1,2,3))   


import urllib.request as r
data=r.urlopen('http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric').read().decode('utf-8','ignore')

import json
data=json.loads(data)




def weather(a,b):
    print('第'+str(a)+'天的天气情况')
    print(data['list'][b]['weather'][0]['main'])
weather(1,2)
weather(2,10)
weather(3,18)
weather(4,26)
weather(5,34)

def temp(a,b):
    print('第'+str(a)+'天的温度')
    print('x'*int(data['list'][b]['main']['temp']))
    return 0
temp(1,2)
temp(2,10)
temp(3,18)
temp(4,26)
temp(5,34)

def weather(a,b):
    print('第'+str(a)+'天')
    print('温度为：'+str(data['list'][b]['main']['temp'])+'最高温度为：'+str(data['list'][b]['main']['temp_max'])+'最低温度为：'+str(data['list'][b]['main']['temp_min'])+'天气情况为：'+str(data['list'][b]['weather'][0]['main']))
weather(1,2)
weather(2,10)
weather(3,18)
weather(4,26)
weather(5,34)

def temp(a):
    ls=data['list'][a]['main']['temp']
    return ls

m1=temp(2)
m2=temp(10)
m3=temp(18)
m4=temp(26)
m5=temp(34)
m=[m1,m2,m3,m4,m5]

print(sorted(m))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

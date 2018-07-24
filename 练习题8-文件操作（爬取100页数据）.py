# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 17:13:28 2018

文件的保存：

   1.创建文件，文件名：喜欢的TV
   2.内容
   3.保存的路径
   4.设置文本格式
   5.保存到硬盘中
文件的打开:
    1.寻找路径
    2.打开文件
    3.读取内容
    4.关闭文件流


@author: chenya
"""

####阅读文件会发生的问题，文字编码的问题，乱码
add=''###文件位置
f=open(add)
ls=f.readlines()  #将文本读取成列表
#s=f.read()   读取文本中所有的字符
f.close()
#######################
f=open('喜欢的手机.txt','w',encoding='utf-8') #write
f.write('华为mate7')
f.close()#关闭保存程序
#########################append-a追加
#######exel打开
f=open('淘宝数据.csv','w',encoding='utf-8') #write
f.write('裙子1,99,10运费,972购买\n')
f.write('袜子1,99,10运费,9999购买\n')
f.close()#关闭保存程序,

练习题8：保存淘宝数据（小组项目）
1.每个组员爬取某个URL的100页数据，每个组员爬取不同城市，上海，北京，成都，郑州，
2.保存商品信息（同练习题6），并且保存为csv格式，
3.每组组长合并组员的数据，后续班级合并数据

import urllib.request as r
data=r.urlopen('https://s.taobao.com/search?initiative_id=staobaoz_20180719&q=%E8%A3%99%E5%AD%90&loc=%E5%9B%9B%E5%B7%9D&ajax=true').read().decode('utf-8','ignore')

import json
data=json.loads(data)
 

for b in range(0,4400,44):
    try:
        url='https://s.taobao.com/search?initiative_id=staobaoz_20180719&q=%E8%A3%99%E5%AD%90&loc=%E5%9B%9B%E5%B7%9D&ajax=true&b={}'
        import urllib.request as r
        data=r.urlopen(url.format(b)).read().decode('utf-8','ignore')
        f=open('淘宝100页-四川.txt','a',encoding='utf-8')
        f.write(data+'\n')
        f.close
    except Exception as err:
        print('爬取异常')
        
for b in range(0,4400,44):
    try:
        url='https://s.taobao.com/search?initiative_id=staobaoz_20180719&q=%E8%A3%99%E5%AD%90&loc=%E5%9B%9B%E5%B7%9D&ajax=true&b={}'
        import urllib.request as r
        data=r.urlopen(url.format(b)).read().decode('gbk','ignore')
        f=open('淘宝100页-四川1.csv','a',encoding='gbk')
        f.write(data+'\n')
        f.close
    except Exception as err:
        print('爬取异常')
      
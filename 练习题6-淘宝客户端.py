# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 11:36:01 2018
练习6：
1.显示四个商品，然后打印分割线，只要第一页36个商品信息
2.列出36个商品
3.获取所有的商品价格，并且给商品排序，从高到低排序
4.按照销量排序
5.商品过滤，只要15天退款或者包邮的商品信息，显示
@author: chenya
"""
import urllib.request as r
data=r.urlopen('https://s.taobao.com/search?initiative_id=staobaoz_20180718&q=%E6%A0%BC%E5%AD%90%E8%A1%AC%E8%A1%AB%E5%A5%B3%E7%9F%AD%E8%A2%96+%E5%AE%BD%E6%9D%BE&suggest=0_1&_input_charset=utf-8&wq=gezichenshannv&suggest_query=gezichenshannv&source=suggest&ajax=true').read().decode('utf-8','ignore')

import json
data=json.loads(data)

print('商品名：'+data['mods']['itemlist']['data']['auctions'][0]['title'])
print('价格：'+data['mods']['itemlist']['data']['auctions'][0]['view_price'])
print('运费为：'+data['mods']['itemlist']['data']['auctions'][0]['view_fee'])
print('销量：'+data['mods']['itemlist']['data']['auctions'][0]['view_sales'])

def goods():
    for a in range(0,4):
        print('第'+str(a+1)+'件商品信息：')
        print('商品名：'+data['mods']['itemlist']['data']['auctions'][a]['title'])
        print('价格：'+data['mods']['itemlist']['data']['auctions'][a]['view_price'])
        print('运费为：'+data['mods']['itemlist']['data']['auctions'][a]['view_fee'])
        print('销量：'+data['mods']['itemlist']['data']['auctions'][a]['view_sales'])
goods()

def goods():
    for a in range(0,36):
        print('第'+str(a+1)+'件商品信息：')
        print('商品名：'+data['mods']['itemlist']['data']['auctions'][a]['title'])
        print('价格：'+data['mods']['itemlist']['data']['auctions'][a]['view_price'])
        print('运费为：'+data['mods']['itemlist']['data']['auctions'][a]['view_fee'])
        print('销量：'+data['mods']['itemlist']['data']['auctions'][a]['view_sales'])
goods()

ls=[]
def price():
    for a in range(0,36):
        c=float(data['mods']['itemlist']['data']['auctions'][a]['view_price'])
        ls.append(c)
    return ls 
price()
print(ls)
e=sorted(ls)
print(e)
f=list(reversed(e))
print(f)

ls=[]
def sales():
    for a in range(0,36):
        c=str(data['mods']['itemlist']['data']['auctions'][a]['view_sales'])
        
        d=int(c[0:-3])
        
        ls.append(d)
    return ls
sales()
print(ls)


x=sorted(ls)
print('商品销量排序为：')
y=list(reversed(x))
print(y)

def goods():
    for a in range(0,36):
        print('第'+str(a+1)+'一件商品邮费为：')
        print(data['mods']['itemlist']['data']['auctions'][a]['view_fee'])
        
goods() 

def fee():
     for a in range(0,36):
         if float(data['mods']['itemlist']['data']['auctions'][a]['view_fee'])==0.00:
             print('第'+str(a+1)+'件商品包邮并且信息为：')
             print('商品名：'+data['mods']['itemlist']['data']['auctions'][a]['title'])
             print('价格：'+data['mods']['itemlist']['data']['auctions'][a]['view_price'])
             print('销量：'+data['mods']['itemlist']['data']['auctions'][a]['view_sales'])
fee()
    









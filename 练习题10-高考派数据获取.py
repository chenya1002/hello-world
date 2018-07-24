# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 17:05:34 2018
请求的URL
http://www.gaokaopai.com/university-ajaxGetMajor.html
求情的数据
id=3319&type=2&city=34&state=1
学校编号   理科2        城市        正常

作业10：
1.获取2300所学校的编号
2.获取31所城市的编号
3.获取142000数据，31/10，每个组3个城市，后面组装在一起
4.将142600数据使用spark统计
@author: Administrator
"""
ls=open('d:\\实训\\all_school.txt',encoding='utf-8').readlines()
schoolls=[]    

for line in ls:
    schoolls.append(line.split('-jianjie-')[1].split('.')[0])
print('学校的编号：',schoolls)


ls1=open('d:\\实训\\XML高考派城市.txt',encoding='gbk').readlines()
cityls=[]
for line in ls1:
     text=line.split(', ')
     if len(text)==2:
         print(text[1].split(')')[1][2:4],text[1].split(')')[0])

import urllib.request as r
f=open('d:\\实训\\全国招生计划表-重庆111111.txt','a',encoding='utf-8')#write
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest'}
for schoolId in schoolls:
    for type in (1,2):
        req=r.Request(url,data='id={}&type={}&city=50&state=1'.format(schoolId,type).encode(),headers=headers)
        try:
            data=r.urlopen(req).read().decode('utf-8','ignore')
            while '<!DOCTYPE html>' in data:
                data=r.urlopen(req).read().decode('utf-8','ignore')
            f.write(data+'\n')
            print('成功')
        except Exception as err:
            print('发生错误')
f.close()#关闭保存程序 







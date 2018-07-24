# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 14:00:42 2018

@author: chenya
"""

ls=open('D:\实训\\文本全国招生计划-重庆.txt',encoding='utf-8').readlines()
schoolls=[]
for line in ls:
    schoolls.append(line.split(',')[0].split('(')[1])
    print(schoolls)
for line in ls:
    schoolls.append(line.split(',')[1].split(')')[0])
    print(schoolls)

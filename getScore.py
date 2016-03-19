# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 21:53:07 2016

@author: small
"""
import numpy as np
import pandas as pd
import os

root_dir = 'C:\\学习\\素拓'
ID = 115032910018
filelist = []
for items in os.walk(root_dir):
    for item in items[2]:
        filelist.append(os.path.join(items[0],item))
filelist = [x for x in filelist if os.path.splitext(x)[1]=='.xlsx']
#filelist = ['2015上海国际马拉松赛志愿者-团委邵宪一（1216更新）.xlsx']
results = pd.DataFrame(columns = ['学号','姓名','指标内容','指标名称','分数'])
for name in filelist:
#    filename = os.path.join(root_dir,name)
    data = pd.read_excel(name)
#    if data['学号'].dtypes != np.int64:

    data['学号'].astype(str)
    
#    data['学号'].astype(np.int64)
        

    result = data[data['学号']==ID]
    results = results.append(pd.DataFrame(result,columns = ['学号','姓名','指标内容','指标名称','分数']))



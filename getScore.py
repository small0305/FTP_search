# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 21:53:07 2016

@author: small
"""
import numpy as np
import pandas as pd
import os

root_dir = 'C:\\学习\\素拓\\党团'
ID = 115032910018
filelist = [x for x in os.listdir(root_dir) if os.path.splitext(x)[1]=='.xlsx']
results = pd.DataFrame(columns = ['学号','姓名','指标内容','分数'])
for name in filelist:
    filename = os.path.join(root_dir,name)
    data = pd.read_excel(filename)
    if data['学号'].dtypes != 'int64':
        
#        data['学号'].astype(str)
        data['学号'] = data['学号'].fillna(0)
        data['学号'].astype(np.int64)
        

    result = data[data['学号'] == ID]
    results = results.append(pd.DataFrame(result,columns = ['学号','姓名','指标内容','分数']))



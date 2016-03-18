# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 21:53:07 2016

@author: small
"""
import numpy as np
import pandas as pd
data = pd.read_excel('20151011-“阳光计划”体验式培训-团委邵宪一.xlsx')
result = data[data['学号'] == 115032910018]
results = pd.DataFrame(result,columns = ['学号','姓名','指标内容','分数'])


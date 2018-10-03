#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 21:47:11 2018

@author: Shaoyu
"""
import json 

#%%

rawdata=open('yelp_academic_dataset_business.json','r')
data=rawdata.readlines()
#%%
interested=[]

for i in data:
    temp=json.loads(i)
    interested.append(temp['city'])
#%%
    
citylist=list(set(interested))
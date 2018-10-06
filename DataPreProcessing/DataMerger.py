#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 16:29:32 2018

@author: Shaoyu
"""
#%%
import pandas as pd
import glob
#%%
# Merge all Data From Data API file
col_names=['name','latitude','longitude','is_closed','zipcode',\
           'city','state','price','rating','url','review_count', \
           'transactions','category','id']
res_api_df  = pd.DataFrame(columns = col_names)
res_api_df.to_csv(r'RawData/Resturant_API_Combined.csv', index=None,sep=',', mode='w')

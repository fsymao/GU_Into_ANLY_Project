#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 16:06:31 2018

@author: Shaoyu
"""

from yelpapi import YelpAPI
import pandas as pd
import numpy as np 
api_key="K5URbDqMy4NUlwDo3ijwez_LDl0mUP2rM_6t4NuXaD2-yXus8a8a5hIha-1YY4uKZUv3JtvawCiNwcZASuw_c3DhkqLHbyI_WBudYr3K_Cc7luMMsm4UZmV-L_SvW3Yx"
yelp_api = YelpAPI(api_key)

#%%
dc_df=pd.read_csv('DC_Resturant.csv')
lat_long_list=dc_df[['latitude','longitude']].values.tolist()
#%%
resultslist=[]
for i in lat_long_list:    
    lat1=i[0]
    long1=i[1]
    response = yelp_api.search_query(term='resturant', \
                                 latitude=lat1,\
                                 longitude=long1,\
                                 radius=20000,
                                 offset=10,
                                 sort_by='distance',
                                 limit=50)
    resultslist.append(response)
 
#%%
col_names=['name','latitude','longitude','is_closed','zipcode',\
           'city','state','price','rating','url','review_count', \
           'transactions','category','id']
my_df  = pd.DataFrame(columns = col_names)
my_df.to_csv(r'DC_Resturant_updated.csv', index=None,sep=',', mode='w')

#%%
for queryresults in resultslist:
    for temp in queryresults['businesses']:
        try:
            res_id=temp['id']
            categories=temp['categories']
            category=""
            for cat in categories:
                category+= cat['alias']+","
            category=category[0:-1]
            name=temp['name']
            lat=temp['coordinates']['latitude']
            long=temp['coordinates']['longitude']
            is_closed=temp['is_closed']
            zipcode=temp['location']['zip_code']
            city=temp['location']['city']
            state=temp['location']['state']
            price=temp['price']
            rating=temp['rating']
            url=temp['url']
            review_count= temp['review_count']
            transactions=temp['transactions']
            my_df=my_df.append({col_names[0]:name,\
                                  col_names[1]:lat,\
                                  col_names[2]:long ,\
                                  col_names[3]:is_closed, \
                                  col_names[4]:zipcode ,\
                                  col_names[5]:city, \
                                  col_names[6]:state, \
                                  col_names[7]:price,\
                                  col_names[8]:rating,\
                                  col_names[9]:url, \
                                  col_names[10]:review_count ,\
                                  col_names[11]:transactions, \
                                  col_names[12]:category, \
                                  col_names[13]:res_id
                                  }, ignore_index=True)
        except:
            continue
#my_df=my_df.drop_duplicates(['id'])
#%%
my_df=my_df.drop_duplicates(['id'])
my_df.to_csv(r'DC_Resturant_updated.csv', index=None, sep=',', mode='a',header=None)

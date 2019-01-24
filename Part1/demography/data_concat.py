#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 15:45:26 2018

@author: Shaoyu
"""

#%%
import pandas as pd 
from glob import glob 

#%%
filenames=glob("demography/data*.csv")
combined_csv=pd.concat( [ pd.read_csv(f,index_col=0) for f in filenames ])
orginial_data=pd.read_csv('RawData/Resturant_Full_Infomation.csv')
final_df=pd.merge(orginial_data,combined_csv, how='left', left_on='zipcode', right_on='Zipcode')
final_df.to_csv('RawData/Full_Information.csv')


# =============================================================================
# # From Listing Point of View 
# # Is Listing Review Counts Affect 
# =============================================================================


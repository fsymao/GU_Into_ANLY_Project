#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 16:29:32 2018
q
@author: Shaoyu
"""
#%%
import pandas as pd
import glob
#%%
# Merge all Data From Data API file
filelist=glob.glob("RawData/DataPulling/*.csv")
combined_csv = pd.concat([pd.read_csv(f) for f in filelist ])
combined_csv.to_csv("RawData/Resturant_API_Combined.csv",index=None,)
#%%
filelist=glob.glob("RawData/DataScrape/*.csv")
combined_csv = pd.concat([pd.read_csv(f) for f in filelist ])
combined_csv.to_csv("RawData/Resturant_Scrape_Combined.csv",index=None,)
#%%
filelist=glob.glob("RawData/GoogleMapAPI/*.csv")
combined_csv = pd.concat([pd.read_csv(f) for f in filelist ])
combined_csv.to_csv("RawData/Resturant_Map_API_Combined.csv",index=None,)
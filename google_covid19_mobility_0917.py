# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 09:41:22 2020

@author: vincent.yu

 df.columns
 df.info(verbose=True)
 df.shape()
 df.head()
 df.describe()
"""
import os

from datetime import datetime
import requests
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

#Read CSV File To dataFrame
csv_file = 'K:\My files\Download\COVID19_Mobility\Global_Mobility_Report_0909.csv'
df = pd.read_csv(csv_file ,header=0,index_col=0, squeeze=True)

#Select Data, Columns 

target_list = ['South Korea','Brazil', 'India','United Kingdom','Germany']



##항목 선택및 순서변경 
# =============================================================================
# column_names = ["date", "country_region","metro_area","retail_and_recreation_percent_change_from_baseline",\
#                 "grocery_and_pharmacy_percent_change_from_baseline", "parks_percent_change_from_baseline", \
#                 "transit_stations_percent_change_from_baseline","workplaces_percent_change_from_baseline",
#                 "residential_percent_change_from_baseline"]
# =============================================================================
column_names = ["date", "country_region","metro_area","retail_and_recreation_percent_change_from_baseline",\
                "parks_percent_change_from_baseline", "workplaces_percent_change_from_baseline"]
    
df = df[column_names]

#Select Target list
result = df[df["country_region"].isin(target_list)]
result["country_region"]=pd.Categorical(result["country_region"], target_list)

#print(result)
#result.plot()
#print(df1.head())
#print("\n")

datestring = datetime.strftime(datetime.now(),'%Y_%m_%d_%H_%M')
result.to_excel('K:\My files\Download\COVID19_Mobility\Covid19_Mobility_' + datestring +'.xlsx')

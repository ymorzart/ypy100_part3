# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 14:20:44 2020

@author: vincent.yu

change DF to CSV, Excel with Date 
"""
import os
os.environ["HTTP_PROXY"] = "http://70.10.15.10:8080"
os.environ["HTTPS_PROXY"] = "http://70.10.15.10:8080"
os.environ["PYTHONHTTPSVERIFY"] = "0"

from datetime import datetime
import requests
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf


csv_file = 'K:/My files/Download/DC_COVID19_4/WHO-COVID-19-global-data.csv'

df1 = pd.read_csv(csv_file ,header=0,index_col=0, squeeze=True)

#df1.plot()
#print(df1)
#print("\n")


datestring = datetime.strftime(datetime.now(),'%Y_%m_%d_%H_%M')
df1.to_csv('K:/My files/Download/DC_COVID19_4/WHO-COVID-19_' + datestring +'.csv')
df1.to_excel('K:/My files/Download/DC_COVID19_4/WHO-COVID-19_' + datestring +'.xlsx')

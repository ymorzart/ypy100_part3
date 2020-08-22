# -*- coding: utf-8 -*-
"""
Created on Tue Jul 7 15:01:32 2020

@author: vincent.yu
"""
import os

# 42

from pytrends.request import TrendReq
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import requests

keywords = ["현대 팰리세이드","쌍용 렉스턴"]
local_area = "KR"
period = "2020-01-01 2020-06-30"

resp = requests.get('https://trends.google.com:443', verify=False) 
#resp = requests.get(base_url, verify = False)
#html_src = resp.text
#soup = BeautifulSoup(html_src,'html.parser')
#print(soup)

#TrendReq(hl='ko', tz=540, timeout=(10,25), proxies=['https://34.203.233.13:80',], retries=2, backoff_factor=0.1, verify=False)
#trend_obj = TrendReq(hl='ko', tz=540, timeout=(10,25), proxies=['https://34.203.233.13:80',], retries=2, backoff_factor=0.1)
trend_obj = TrendReq()
trend_obj.build_payload(kw_list = keywords, timeframe = period,geo = local_area)

trend_df = trend_obj.interest_over_time()
trend_df = trend_df.reset_index()
trend_df['Date'] = trend_df['date'].dt.to_period(freq='W')
trend_df.set_index('Date',inplace=True)

trend_df.drop(['date', 'isPartial'], axis=1, inplace=True)
print(trend_df.head())
print("\n")

#https://finance.yahoo.com/
hd = pd.read_csv("C:/Vincent/Devops/Spyder Projects/Start of June/finance/005380.KS.csv", index_col=0, encoding='utf-8')
sy = pd.read_csv("C:/Vincent/Devops/Spyder Projects/Start of June/finance/003620.KS.csv", index_col=0, encoding='utf-8')
print(hd.head())
print("\n")

print(sy.head())
print("\n")


def min_max_scaler(x):
    return(x - x.min()) / (x.max() - x.min())

hd['Scaled_Adj'] = hd[['Adj Close']].apply(min_max_scaler)
sy['Scaled_Adj'] = sy[['Adj Close']].apply(min_max_scaler)
hd_df = hd.iloc[1:, :]
sy_df = sy.iloc[1:, :]

print(hd_df.head())
print("\n") 

trend_df.index = hd_df.index
print(trend_df.head())
print("\n")

final_data = pd.concat([trend_df, hd_df['Scaled_Adj'], sy_df['Scaled_Adj']], axis=1)
final_data.columns = ['펠리세이드','렉스턴','현대','쌍용']
print(final_data.head())
print("\n")

from matloptlib import font_manager, rc
font_path = os.path.join(os.getcwd(),"data","malgun.ttf")
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font',family=font_name)

plt.style.use("ggplot")
ax1 = final_data[['펠리세이드','렉스턴']].plot(kind='bar',figsize=(20,10))
ax2 = ax1.twin()

final_data[['현대','쌍용']].plot(ls='--', ax=ax2)
ax1.legend(loc="upper right")
ax2.legend(loc="upper center")
plt.title("구글 검색 트렌드 관계",size=18)

#현 작업 디렉토리
print("현재 폴더: ", os.getcwd())
# 디렉토리 변경 
os.chdir("K:/My files/Download/wordCloud")
print("변경 폴더: ", os.getcwd())

#화일명에 현재 일자 포함
#datestring = datetime.strftime(datetime.now(),'%Y_%m_%d_%H_%M_%S')
#plt.savefig('K:/My files/Download/wordCloud/Word_'+ datestring +'.png')

output_filepath = os.path.join(os.getcwd(),"output", "google_trend_stock_price.png")
plt.savefig(output_filepath,dpi=300)

plt.show()

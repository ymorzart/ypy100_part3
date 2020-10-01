# -*- coding: utf-8 -*-
"""
Created on Mon Aug  4 10:54:47 2020

@author: vincent.yu
Source for WHO Global Data
Target Countries Data Center Area 
Create 2개 엑셀화일 전세계 216개국 순위, 센터권역 순위
"""
import os
# os.environ["HTTP_PROXY"] = "http://70.10.15.10:8080"
# os.environ["HTTPS_PROXY"] = "http://70.10.15.10:8080"
# os.environ["PYTHONHTTPSVERIFY"] = "0"

import pandas as pd
from datetime import datetime
import requests


df = pd.read_csv('https://covid19.who.int/WHO-COVID-19-global-data.csv')
#df1 = pd.read_csv(csv_file ,header=0,index_col=0, squeeze=True)


target_list = ['Republic of Korea','United States of America', 'Brazil', 'India', 'Russian Federation', 'The United Kingdom' \
                 ,'Germany','China','Singapore','Viet Nam']

#column_names = ["Date_reported"," Country"," New_cases", " Cumulative_cases", " New_deaths", " Cumulative_deaths"]

##항목 선택및 순서변경 
column_names = [" Country"," Cumulative_cases"," New_cases", " New_deaths", " Cumulative_deaths"]

# sort_value 데이터 정렬 
#df = df.sort_values(by=['cust_no', 'update_dt', 'age_gender'])

#최종일 기준 확진자수로 정렬 

df = df.groupby(' Country').apply(lambda x: x[x['Date_reported'] == x['Date_reported'].max()]).reset_index(drop=True)
df = df[column_names]
df = df.sort_values(by=[' Cumulative_cases'],axis=0, ascending=False).reset_index(drop=True)

# 순위 기입
df = df.reset_index()
df["index"] = df["index"]+1

##Total 항목이름 변경 
result = df.rename(columns={"index":"순위"," Country":"국가"," Cumulative_cases":"누적확진자", \
                          " New_cases":"신규확진자"," New_deaths":"신규사망자"," Cumulative_deaths":"누적사망자" })

# Total 
datestring = datetime.strftime(datetime.now(),'%Y_%m_%d_%H_%M')
result.to_excel('C:/Vincent/Devops/Spyder Projects/Mid of Aug/DC_COVID19_8/WHO-COVID-19_Total_'+ datestring +'.xlsx'\
              ,index=False,startrow=1, startcol=1,)

##DC권역 선정 국가만 나열 
result = df[df[" Country"].isin(target_list)]
result[" Country"]=pd.Categorical(result[" Country"], target_list)
#df = result.sort_values(" Country").reset_index(drop=True)


# 순위 기입
#df = df.reset_index()
#df = result.reset_index()
#df["index"] = df["index"]+1

#항목이름 변경 
result = result.rename(columns={"index":"순위"," Country":"국가"," Cumulative_cases":"누적확진자", \
                          " New_cases":"신규확진자"," New_deaths":"신규사망자"," Cumulative_deaths":"누적사망자" })

print(result)

#날짜포홤 엑셀저장
datestring = datetime.strftime(datetime.now(),'%Y_%m_%d_%H_%M')
result.to_excel('C:/Vincent/Devops/Spyder Projects/Mid of Aug/DC_COVID19_8/WHO-COVID-19_DC_Area_'+ datestring +'.xlsx'\
              ,index=False,startrow=1, startcol=1,)

# datestring = datetime.strftime(datetime.now(),'%Y_%m_%d_%H_%M')
# df1.to_csv('K:/My files/Download/DC_COVID19_4/WHO-COVID-19_' + datestring +'.csv')
# df1.to_excel('K:/My files/Download/DC_COVID19_4/WHO-COVID-19_' + datestring +'.xlsx')

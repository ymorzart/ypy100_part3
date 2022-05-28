# -*- coding: utf-8 -*-
"""
22.05.28 Korea 발췌, 기간설정, 엑셀저장 완료
22.05.27 WHO Covid19 Korea추이 분석 - 기간설정 
22.05.26 WHO Covid19 추이분석 - 시각화 
01/21 배치로 일일 수행 중 
Created on Mon Aug  4 10:54:47 2020
@author: vincent.yu
Source for WHO Global Data
Target Countries Data Center Area 
Create 2개 엑셀화일 전세계 216개국 순위, 센터권역 순위
"""
import os
os.environ["HTTP_PROXY"] = "http://70.10.15.10:8080"
os.environ["HTTPS_PROXY"] = "http://70.10.15.10:8080"
os.environ["PYTHONHTTPSVERIFY"] = "0"

import pandas as pd
from datetime import datetime
import requests
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import numpy as np
import matplotlib.ticker as ticker



df = pd.read_csv('https://covid19.who.int/WHO-COVID-19-global-data.csv')
#df1 = pd.read_csv(csv_file ,header=0,index_col=0, squeeze=True)

# #필터링 국가 선정 상황에 따라 case1, case2 선택 가능 
# #국가 선정 Case1 -> list로 
# target_list = ['Republic of Korea']
# #선정 국가만 나열 
# df = df[df["Country"].isin(target_list)]
# df["Country"]=pd.Categorical(df["Country"], target_list)
# df = df.sort_values("Country").reset_index(drop=True)

#국가 선정 Case2 ->  Query 상세조건 
str_expr = "(Country == 'Republic of Korea')"  
# 데이터 Query, 인덱스 초기화 실시(drop=True하면,dataframe내에서 삭제)
df = df.query(str_expr) #.reset_index(drop=True) 

#항목 선택및 순서변경 
column_names = ["Date_reported","Country","Cumulative_cases","New_cases", "New_deaths", "Cumulative_deaths"]

# 선택한 항목만 지정 (기존 항목은 제외)
df = df[column_names]


#날짜 기간 지정 
df = df.query("Date_reported >= '2022-01-01' and Date_reported <='2022-05-26'") # OK

#df = df.query("Date_reported >= '2022-05-1' and Date_reported=최신날짜") # 데이터의 최신날짜를 검색 추가 검토 필요
#df =df.loc[df["Date_reported"].between('2022-05-01', '2022-05-26')]    # OK

# sort_value 데이터 정렬
#날짜로 정렬, 기존의 행 인덱스를 제거하고 데이터열중 하나를 인덱스로 설정  
df = df.sort_values(by=["Date_reported"],axis=0, ascending=True).reset_index(drop=True) 

#Date를 인덱스로 지정, set_index() -> 기존의 행 인덱스를 제거하고 인덱스를 데이터 열로 추가 
#inplace=True하면 원본객체 변경, drop=False 인덱스 지정열을 데이터열에 추가(주요 포인트)
df.set_index('Date_reported',drop=False) 
#df.set_index('Date_reported',inplace = True, drop=False) #인덱스지정 컬럼이 아래항목에 표시(에러)

#최종일기준 누적확진자수로 정렬 ->  필터링(lamda x:  조건(최종일))
#df = df.groupby('Country').apply(lambda x: x[x['Date_reported'] == x['Date_reported'].max()]).reset_index(drop=True)
#df = df[column_names]
#df = df.sort_values(by=['Cumulative_cases'],axis=0, ascending=False).reset_index(drop=True)


#print(df)

# #시각화 (22.05.27)
# # fi,ax = plt.subplots()
# # ax.scatter(x=result['Date_reported'], y=result['New_cases'])
# # #dateFmt = mdates.DateFormatter('%Y-%m-%d')
# # #ax.xaxis.set_major_formatter(dateFmt)
# # #plt.grid()
# # plt.show()


# # default plot 시각화 
# #df.plot()

# # 한글 폰트 사용을 위해서 설정 
# from matplotlib import font_manager, rc
# font_path = "C:/Windows/Fonts/NGULIM.TTF" #PC Windows 설치 위치 확인 
# font = font_manager.FontProperties(fname=font_path).get_name()
# rc('font', family=font)

# # y축 설정 
# df.plot(y=['New_cases'] )
# # #result.plot(y=['Date_reported','Cumulative_cases'])
# # 타이틀 
# plt.title("예제: Covid19 trends")

# # plt.figure(figsize=(10, 6))
# plt.grid(axis='both')
# #
# plt.xlabel("날짜: Date", labelpad=10)
# plt.ylabel("인원(명):Cases", labelpad=10)
# # 간격, 범위 
# plt.ylim(0,700000) #Y축 범위 
# #plt.yticks(np.arange(0,7))

# # X=np.array([1,1000000])
# # Y=np.array([1,1000000])
# # plt.plot(X,Y,color='None')
# # ax=plt.axes()
# # ax.xaxis.set_major_locator(ticker.MultipleLocator(100))
# # ax.yaxis.set_major_locator(ticker.MultipleLocator(100))
# #ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))
# #ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.5))

# plt.show()


#엑셀 저장시 한글로 항목이름 변경 
result = df.rename(columns={"Date_reported":"날짜","Country":"국가","Cumulative_cases":"누적확진자",\
                            "New_cases":"신규확진자","New_deaths":"신규사망자","Cumulative_deaths":"누적사망자" })
                   #index={"Date_reported":"날짜"}) #나중에 인덱스명 변경 추가  학습필요
print(result)
    
#날짜포홤 엑셀저장
datestring = datetime.strftime(datetime.now(),'%Y_%m_%d_%H_%M')
result.to_excel('K:/My files/Download/DC_COVID19_4/WHO-COVID-19_Korea_'+ datestring +'.xlsx'\
              ,index=False, startrow=1, startcol=1) #index = false하면 지정된 인덱스열이 지워짐

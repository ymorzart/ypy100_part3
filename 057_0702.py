# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 16:01:39 2020

@author: vincent.yu
"""
import os


import openpyxl
import pandas as pd 
from datetime import datetime

datestring = datetime.strftime(datetime.now(),'%Y_%m_%d_%H_%M')
#datestring = datetime.strftime(datetime.now(),'%Y_%m_%d_%H_%M_%S')
#현 작업 디렉토리
print("현재 폴더: ", os.getcwd())
# 디렉토리 변경 
os.chdir("K:/My files/Download/Ex_0702")
print("변경 폴더: ", os.getcwd())

dict_data = {'c0':[1,2,3],'c1':[4,5,6]}
df = pd.DataFrame(dict_data, index=['r0','r1','r2'])
print(df,"\n")

#df.to_excel("./output/df.xlsx")
df.to_excel('K:/My files/Download/Ex_0702/output/df_' + datestring + '.xlsx')

cwd = os.getcwd()
filename = "df.xlsx"
filepath = os.path.join(cwd, "output", filename)

wb = openpyxl.load_workbook(filepath)

print(wb)
print(type(wb))
print(wb.sheetnames)

ws = wb['Sheet1']
print(ws)
print(ws.title)


active_sheet = wb.active
print(active_sheet)

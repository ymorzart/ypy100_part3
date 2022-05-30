# -*- coding: utf-8 -*-
"""
Created on Mon May 30 11:31:39 2022

@author: ymorzart
"""
import pandas as pd


df = pd.DataFrame({'X':[1,2,7,4,10], 'Y':[4,3,8,2,9], 'Z':[2,7,6,10,5]})

print("Dataframe:")
print(df)

#%%
#각 행의 최대값
max_row = df.max(axis=1)
print("행 최대값")
print(max_row)

#%%
#x,y각 열의 최대값 default는 axis=0
maxs = df.max()
print("각 열의 최대값")
print(maxs)
#%%

#%%
# X열이 최대값이 행 전체 
df = df.loc[lambda x: x['X'] == x['X'].max()]
print("X가 최대값인 행출력,y는 상관없이" )
print(df)
#%%

#X가 최대값
maxX = df["X"].max()
print("X열의 최대값")
print(maxX)


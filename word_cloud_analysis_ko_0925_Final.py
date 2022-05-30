# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 10:03:31 2020

@author: vincent.yu
"""
import os

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

from datetime import datetime

from PIL import Image
import numpy as np
import json

#현 작업 디렉토리
print("현재 폴더: ", os.getcwd())
# 디렉토리 변경 
os.chdir("K:/My files/Download/WordCloud_KO")
print("변경 폴더: ", os.getcwd())

# 1. 별도 작성된 문서자료 읽어서 분석 할때 사용
file_name = str(input("분석할 화일명을 입력하세요:"))
text = open(file_name,encoding='utf-8').read()

# 2. Text 직접 입력
# text = "파이썬 워드클라우드 파이썬 좋아 워드클라우드 파이썬 \
#         라이브러리 좋아 파이썬 워드클라우드 예시 워드클라우드 워드클라우드"

# 3. 한글문서로 입력변수로 분석 
#text = open('K:\My files\Download\WordCloud_KO\ko_ana.txt', encoding='utf-8').read()   
     
        
#text 입력변수 분석
#wordcloud = WordCloud(font_path='C:\Windows\Fonts\malgun.ttf', background_color='white',
#                      width = 1920,
#                      height = 1080).generate(text)

# =============================================================================
# text = ['이것 은 예문 입니다', '여러분 의 문장을 넣 으세요']
# keywords = {'이것':5, '예문':3, '단어':5, '빈도수':3}
# stopwords = {'은','입니다'}
# wordcloud = WordCloud(stopwords=stopwords)
# wordcloud = wordcloud.generate_from_text(text)
# wordcloud = wordcloud.generate_from_frequencies(keywords)
# 
# =============================================================================
#제외단어 제거 
#stopwords = set(STOPWORDS) 

#stopwords = {'운영','필요','진행','영역','절실'}
stopwords = {'것입니다','위한','합니다','있습니다','위해','되었습니다','우리는','모든'}
#stopwords.add('필요') 
wordcloud = WordCloud(font_path='C:\Windows\Fonts\malgun.ttf', background_color='white',
                      stopwords=stopwords, width = 1920, height = 1080).generate(text)

fig = plt.figure(figsize=(22,22)) #이미지 사이즈 지정
plt.imshow(wordcloud, interpolation='bilinear',cmap='YlOrBr')
plt.axis('off') #x y 축 숫자 제거
#plt.show() 


#화일생성및  현재일자포함 
datestring = datetime.strftime(datetime.now(),'%Y_%m_%d_%H_%M_%S')
plt.savefig('K:\My files\Download\WordCloud_KO\Word_'+ datestring +'.png')
#plt.savefig('K:/My files/Download/wordCloud/Word_'+ file_name + datestring +'.png')

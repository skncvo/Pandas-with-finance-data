import pandas as pd
import numpy as np

path = "C:/Users/82108/Desktop/2nd winter/Pandas/Data/삼성전자 종가.csv"

# index_col = 0 == 첫 번째 값을 인덱스로이용
# index_col = 1 == 두 번째 값을 인덱스로이용
# header = 0 == csv파일 안의 첫번째 값
# read_csv를 부를때 squeeze가 true면 series 아니면 dataframe
samsung_price = pd.read_csv(path, index_col= 0, header= 0).squeeze(True)

# '특정 날짜'의 data값을 불러오기
if '2020-12-15' in samsung_price:
    print(samsung_price.loc['2020-12-15'])

# '특정 인덱스'의 data값 불러오기
print(samsung_price.iloc[10])

# samsung_price의 길이
print(samsung_price.shape)

# samsung_price의 값 바꾸기
samsung_price.loc['2020-12-15'] = 70000
print(samsung_price.loc['2020-12-15'])

# 두 개의 Series 연결
path_series_samsung = "C:/Users/82108/Desktop/2nd winter/Pandas/Data/samsung_excel.xlsx"
series1_samsung = pd.read_excel(path_series_samsung, sheet_name= 'Sheet1', index_col= 0).squeeze(True)
series2_samsung = pd.read_excel(path_series_samsung, sheet_name= 'Sheet2', index_col= 0).squeeze(True)
series_samsung = pd.concat([series1_samsung, series2_samsung], ignore_index = False)

# series의 고점과 저점
print(series_samsung.max())
print(series_samsung.min())

# numpy의 array의 인덱스 값이 나오기 떄문에 [0]을 붙어야됨.
# .max()는 값 하나, .values는 np.array이다. 이 둘의 비교가 가능한 이유는 브로드 캐스팅 덕분
print(series_samsung.index[series_samsung.max() == series_samsung.values][0])


# series의 고점과 저점의 인덱스 찾기
print(series_samsung.iloc[series_samsung.argmax()]) #값
print(series_samsung.index[series_samsung.argmax()]) #인덱스

# series의 통계치
print(series_samsung.describe())

# 수익률 == (값 - 전날 값)전날 값 == pct_change()
# (series_samsung - series_samsung.shift(1))/series_samsung.shift(1)
samsung_return = series_samsung.pct_change()
samsung_return = samsung_return * 100 # %로 변환
print(samsung_return.max()) # 최대 수익률
print(samsung_return.index[samsung_return.argmax()]) # 최대 수익률 낸 날짜

# values가 특정 조건을 만족할 때
print(samsung_return[samsung_return>=4]) # 인덱스와 값
print(samsung_return.index[samsung_return >= 4]) # 인덱스
print(samsung_return.values[samsung_return >= 4]) # 값
print(sum(samsung_return[samsung_return>=4])) # 개수

#np.where(조건문, 참일때 값, 거짓일 때 값) == npdarray를 만듦, 새로운 시리즈 생성
samsung_return_over = pd.Series(np.where(samsung_return >=4, "Over 4%", "Under"))
samsung_return_over.index = samsung_return.index
print(samsung_return_over)

# NaN 값
samsung_return.dropna() #NaN 값 제거
samsung_return.fillna(0) #NaN 값 채우기

# 정렬
# index 순으로 정렬, ascending = True : 오름차순, ascending = False : 내림차순
samsung_price.sort_index(ascending = True)
print(samsung_price.sort_index(ascending = False))
# value 순으로 정렬, ascending = True : 오름차순, ascending = False : 내림차순
samsung_price.sort_values()
print(samsung_price.sort_values(ascending = False))



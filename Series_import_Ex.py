import pandas as pd

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
series_samsung.max()
series_samsung.min()
print(series_samsung.index[series_samsung.values == series_samsung.max()]) #argmax 쓰셈

# series의 고점과 저점의 인덱스 찾기
print(series_samsung.iloc[series_samsung.argmax()]) #값
print(series_samsung.index[series_samsung.argmax()]) #인덱스

# series의 통계치
print(series_samsung.describe())


import pandas as pd

path = "C:/Users/82108/Desktop/2nd winter/Pandas/Data/삼성전자 종가.csv"

# index_col = 0 == 첫 번째 값을 인덱스로이용
# index_col = 1 == 두 번째 값을 인덱스로이용
# read_csv를 부를때 squeeze가 true면 series 아니면 dataframe
# header = 0 == csv파일 안의 첫번째 값
pd.read_csv(path , index_col= 0, squeeze = True, header=0 )
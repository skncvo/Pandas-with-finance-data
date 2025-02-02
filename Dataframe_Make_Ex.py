import pandas as pd

# List 
ls = ["a", "b", "c", "d", "e"]
ls_df1 = pd.DataFrame(ls)
ls_df1.index = [1,2,3,4,5]
ls_df1.columns = ["ㅂㅇ"]

# [] 잘 쓰기 
ls_df2 = pd.DataFrame(ls, index=[1,2,3,4,5], columns=["ㅎㅇ"])


# Dictionary
dic = {"a": 101, "b":102, "c":102}
dic_df = pd.DataFrame(dic, index =[0])
print(dic_df)
# dic value를 한 차원에 넣고, 행을 key로 지정
dic_df2 = pd.DataFrame([dic.values()])
dic_df2.columns = dic.keys()
print(dic_df2)

samsung = pd.read_csv()
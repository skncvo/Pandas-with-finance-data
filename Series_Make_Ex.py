import pandas as pd

#Data type이 list인 경우
ls1 = [1,2,3,4,5,6,7,8,9]
ls2 = [1,2,3,'nw','holi',6,7,8,9]

sr1 = pd.Series(ls1)
sr2 = pd.Series(ls2)

# print(sr1)
# print(sr2)

#Data type이 dictionary인 경우
dic1 = {"A": 1, "B": 2, "C": 3}

sr3 = pd.Series(dic1)

print(sr3)
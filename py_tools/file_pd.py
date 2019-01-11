# coding=utf-8

import pandas as pd

liststr=[]
with open("foo.txt") as file:
    for line in file:
        # print(line)
        linelist=line.strip('\n').split(":")
        # print(linelist)
        liststr.append(linelist)

df = pd.DataFrame(liststr, columns=['id','user','site','day'])


print("----- 汇总透视 ----")
print(df.groupby('day')['user'].value_counts())
print("-----count(distinct user )-------")
print(df['user'].value_counts().shape[0])
print("----count(distinct user) group by day --")
print(type(df.groupby('day').agg({'user': pd.Series.nunique})))
print(df.groupby('day').agg({'user': pd.Series.nunique}))


df.groupby('day').agg({'user': pd.Series.nunique}).to_csv("1.csv")
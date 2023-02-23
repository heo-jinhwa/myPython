# Pandas Tutorial - 데이터프레임 생성하기
import pandas as pd

print('1) Dictionary로 DataFrame 만들기')
friend_dict_list = [
    {'name':'John', 'age':25, 'job':'student'},
    {'name':'Nate', 'age':30, 'job':'teacher'}
]
df1 = pd.DataFrame(friend_dict_list) # from_dict로 생성해도 됨
df1 = df1[['name', 'age', 'job']] # key의 순서가 보장되지 않아서 Column을 지정해줘야 함
print(df1.head())
print()

print('2) Ordered Dictionary로 DataFrame 만들기')
from collections import OrderedDict # key의 순서가 보장됨
friend_ordered_dict = OrderedDict(
    [
        ('name', ['John', 'Nate']),
        ('age', [25, 30]),
        ('job', ['student', 'teacher'])
    ]
)
df2 = pd.DataFrame.from_dict(friend_ordered_dict) # from_dict 빼도 상관없음
print(df2.head())
print()

print('3) list로 DataFrame 만들기')
friend_list = [
    ['John', 20, 'stduent'],
    ['Nate', 30, 'teacher']
]
column_name = ['name', 'age', 'job']
df3 = pd.DataFrame(friend_list, columns=column_name)
print(df3.head())
print()

print('4) Series 결합으로 DataFrame 만들기')
s1 = pd.core.series.Series([1, 2, 3])
s2 = pd.core.series.Series(['one', 'two', 'three'])
df4 = pd.DataFrame(data=dict(num=s1, word=s2)) # Series로 DataFrame 만들기
print(df4.head(1))
print(df4.tail(1))
print()

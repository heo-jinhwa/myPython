# Pandas Tutorial - 파일에서 데이터 불러오기
import pandas as pd

print("1) DataFrame 불러오기 및 데이터 확인")
df1 = pd.read_csv('./data/friend_list.csv') # csv파일에서 불러오기
df1 = pd.read_csv('./data/friend_list.txt') # txt파일에서 불러오기
df1 = pd.read_csv('./data/friend_list_tab.txt', delimiter='\t') # txt파일에서 tab을 구분자로 가져오기
print(df1.head(3))
print(df1.tail(2))
print()

print('2) DataFrame 불러오기 및 데이터 확인(head) 없는 경우')
df2 = pd.read_csv('./data/friend_list.csv', header=None) # Column 없이 csv파일 불러오기
df2.columns = ['name', 'age', 'job']
df2 = pd.read_csv('./data/friend_list.csv', header=None, names=['name', 'age', 'job']) # Column 없이 csv파일 불러오고 Column 설정해주기

print('3) Series는 Pandas의 Column')
# 각각의 컬럼은 Series (python에서의 list를 사용)
print(type(df1.name))
print(type(df1.age))
print(type(df1.job))
print()
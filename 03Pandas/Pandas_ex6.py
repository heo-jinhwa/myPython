# Pandas Tutorial - 데이터프레임 행, 열(row, column) 생성, 수정하기
import pandas as pd
import numpy as np

def create_dataframe(header=True):
    print("======== 데이터프레임 생성 시작 ========")
    friend_dict_list = [
        ['John', 20, 'student'],
        ['Jenny', 30, None],
        ['Nate', 30, 'teacher']
    ]
    if header:
        df = pd.DataFrame(friend_dict_list, columns=['name', 'age', 'job'])
    else:
        df = pd.DataFrame(friend_dict_list)
    print(df.head())
    print("======== 데이터프레임 생성 완료 ========")
    print()
    return df

print('1) 열 추가')
df = create_dataframe()
df['salary'] = 0 # salary 열 추가
print(df)

print('2) 열 수정')
df['salary'] = np.where(df['job'] != 'student', 'yes', 'no') # job이 student인 학생만 salary no
print(df)

print('3) 열의 값 추가, 수정, 변형')
friend_dict_list = [
    {'name':'John', 'midterm':95, 'final':85},
    {'name':'Jenny', 'midterm':85, 'final':80},
    {'name':'Nate', 'midterm':30, 'final':10}
]
df = pd.DataFrame(friend_dict_list, columns=['name', 'midterm', 'final'])
df['total'] = df['midterm']+df['final']
df['average'] = df['total']/2
print(df)

grades = []
for row in df['average']:
    if row >= 90:
        grades.append('A')
    elif row >= 80:
        grades.append('B')
    else:
        grades.append('F')
print(grades)
df['grade'] = grades
print(df)

def pass_or_fail(row):
    if row != 'F':
        return "Pass"
    else:
        return "Fail"

df['grade'] = df['grade'].apply(pass_or_fail) # apply함수에 특정 함수를 인자로 넣어서 적용
print(df)

print('4) feature extraction')
date_list = [
    {'yyyy-mm-dd':'2000-06-27'},
    {'yyyy-mm-dd':'2007-10-27'}
]
df = pd.DataFrame(date_list, columns=['yyyy-mm-dd'])
print(df)

def extract_year(row):
    return row.split('-')[0]

df['year'] = df['yyyy-mm-dd'].apply(extract_year)
print(df)

print('5) Row feature extraction')
friend_dict_list = [
    {'name':'John', 'midterm':95, 'final':85},
    {'name':'Jenny', 'midterm':85, 'final':80},
    {'name':'Nate', 'midterm':30, 'final':10}
]
df = pd.DataFrame(friend_dict_list, columns=['name', 'midterm', 'final'])
print(df)
df2 = pd.DataFrame([['Ben', 50, 50]], columns=['name', 'midterm', 'final'])
print(df2)
df = pd.concat([df, df2], axis=0, ignore_index=True) # 2개의 DataFreme을 합치기
print(df)
# Pandas Tutorial - 데이터프레임 행, 열(row, column) 삭제하기
import pandas as pd

def create_dataframe(header=True):
    print("======== 데이터프레임 생성 시작 ========")
    friend_dict_list = [
        ['John', 20, 'stduent'],
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

print('1) name을 index로 하는 DataFrame 만들기')
friend = [
    {'age':15, 'job':'student'},
    {'age':25, 'job':'developer'},
    {'age':30, 'job':'teacher'}
]

df = pd.DataFrame(friend, index=['John', 'Jenny', 'Nate'], columns=['age', 'job'])
print(df)
print()

print('2) 없애고 싶은 index 이름으로 삭제')
# df = df.drop(['John', 'Nate'])
df.drop(['John', 'Nate'], inplace=True) # John, Nate 삭제
print(df)
print()

print('3) 없애고 싶은 index 삭제 ')
df = create_dataframe()
df.drop(df.index[[0, 2]], inplace=True) # 0, 2 index 삭제
print(df)
print()

print('4) 특정 조건 삭제')
df = create_dataframe()
df.drop('age', axis=1, inplace=True) # Column 기준
print(df)





# Pandas Tutorial - 데이터프레임 행, 열(row, column) 선택 및 필터하기
import pandas as pd

def create_dataframe(header=True):
    print("======== 데이터프레임 생성 시작 ========")
    friend_dict_list = [
        ['John', 20, 'stduent'],
        ['Jenny', 30, None],
        ['Nate', 30, 'teacher']
    ]
    if header:
        df = pd.DataFrame(friend_dict_list, columns=['name', 'age', 'job'], index=False)
    else:
        df = pd.DataFrame(friend_dict_list)
    print(df.head())
    print("======== 데이터프레임 생성 완료 ========")
    print()
    return df

print('1) 특정 범위 행만 가져오기')
df = create_dataframe()
df = df[1:3] # 1, 2 index만 가져옴
print(df)
print()

print('2) 특정 행만 가져오기 - loc 사용')
df = create_dataframe()
df = df.loc[[0, 2]] # ★★★ 0, 2번째 행만 가져오기
print(df)
print()

print('3) 특정 조건 행만 가져오기')
df = create_dataframe()
print(df[df.age > 25]) # 나이가 25살 이상인 사람
print(df.query('age > 25')) # 나이가 25살 이상인 사람
print()

print(df[(df.age > 25) & (df.name == 'Nate')]) # 나이가 25살 이상인 사람이고, 이름이 Nate인 사람

print('4) 특정 열만 가져오기 - iloc 사용')
df = create_dataframe(False)
print(df.iloc[:, 0:2]) # ★★★ row index, column index 특정 범위만 가져오기
print(df.iloc[0:2, 0:2])

print('5) 특정 열만 가져오기 - column name 사용')
df = pd.read_csv('./data/friend_list_no_head.csv', header=None, names=['name', 'age', 'job'])
print(df)
print()
 
print(df[['name', 'age']]) # name과 age 열만 가져옴
print()

print(df.filter(items=['age', 'job'])) # name과 age 열만 가져옴 (filter 함수 사용)
print()

print(df.filter(like='a', axis=1)) # column에 a가 들어가는 column만 추출 / axis=1 -> column을 기준으로 한다는 의미
print()

print(df.filter(regex='e$', axis=1)) # b로 끝나는 column만 추출 (정규식 사용)

# Pandas Tutorial - 데이터프레임 파일로 저장하기(to_csv)
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

print('1) 데이터프레임을 csv로 저장하기')
df = create_dataframe()
df.to_csv('./data/friends_save.csv', index=True, header=True, na_rep='-') # Default, None 값은 '-'를 넣어줌

from RPA import RPA
from Process import Process
CONNECTION_PATH = "D:/Uipath/PythonData/PythonConnection.xlsx" # 해당 경로 고정

def main_process(RPAobject):
    pass

if __name__ == '__main__':
    try:
        myRPA = RPA(CONNECTION_PATH)
    except:
        raise Exception(CONNECTION_PATH+" 파일을 확인해주세요.")
    
    print("Python RPA 수행 시작")
    main_process(myRPA)
    print("Python RPA 수행 완료")
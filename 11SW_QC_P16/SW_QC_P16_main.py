from RPA import RPA
from ModviewProcess import ModviewProcess
CONNECTION_PATH = "D:/Uipath/PythonData/PythonConnection.xlsx" # 해당 경로 고정

def main_process(RPAobject):
    ModviewProcess()

if __name__ == '__main__':
    try:
        myRPA = RPA(CONNECTION_PATH)
    except:
        raise Exception(CONNECTION_PATH+" 파일을 확인해주세요.")
    
    print("Python RPA 수행 시작")
    main_process(myRPA)
    print("Python RPA 수행 완료")
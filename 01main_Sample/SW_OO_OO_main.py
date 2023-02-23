from RPA import RPA
from Process import Process
CONNECTION_PATH = "D:/Uipath/PythonData/PythonConnection.xlsx" # 해당 경로 고정

def main_process(RPAobject):
    pass

if __name__ == '__main__':
    print("Python RPA 수행 시작")
    myRPA = RPA(CONNECTION_PATH) 
    # Python 자동화 시작 #    
    main_process(myRPA)
    # Python 자동화 완료 #
    print("Python RPA 수행 완료")
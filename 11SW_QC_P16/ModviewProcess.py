import pyautogui
import time

def ModviewProcess(): 
    pyautogui.click(pyautogui.locateOnScreen("D:/Uipath/SW_QC_P16/data/master/img_data/Plus.PNG")) # 최초 Plus 클릭
    time.sleep(1.5)
    
    Check_Before = len(list(pyautogui.locateAllOnScreen("D:/Uipath/SW_QC_P16/data/master/img_data/Plus.PNG"))) # Plus 개수 확인

    pyautogui.click(pyautogui.locateOnScreen("D:/Uipath/SW_QC_P16/data/master/img_data/FinalShape.PNG"), button='right') # Final Shape 우클릭
    time.sleep(1.5)
    pyautogui.click(pyautogui.locateOnScreen("D:/Uipath/SW_QC_P16/data/master/img_data/Level_Expand.PNG")) # 레벨확장 클릭
    time.sleep(1.5)
    pyautogui.click(pyautogui.locateOnScreen("D:/Uipath/SW_QC_P16/data/master/img_data/Level_1.PNG")) # 레벨1 클릭
    time.sleep(1.5)

    Check_After = len(list(pyautogui.locateAllOnScreen("D:/Uipath/SW_QC_P16/data/master/img_data/Plus.PNG"))) # Plus 개수 확인
    
    print(Check_Before, Check_After)

    if Check_After < Check_Before: # 도면이 하나도 없다? # 예외처리
        return
    
    # 한개 먼저 작업
    pyautogui.press('down')
    time.sleep(1.5)
    pyautogui.click(pyautogui.locateOnScreen("D:/Uipath/SW_QC_P16/data/master/img_data/Analysis.PNG")) # 분석 클릭
    time.sleep(1.5)
    pyautogui.click(pyautogui.locateOnScreen("D:/Uipath/SW_QC_P16/data/master/img_data/Mat.PNG")) # 물적 속성 클릭
    time.sleep(1.5)
    pyautogui.click(pyautogui.locateOnScreen("D:/Uipath/SW_QC_P16/data/master/img_data/Cal.PNG")) # 계산 클릭
    
    if Check_After > Check_Before: # 도면 2개 확인
        pyautogui.click(pyautogui.locateOnScreen("D:/Uipath/SW_QC_P16/data/master/img_data/ModelBrowser.PNG")) # 모델브라우저 클릭
        time.sleep(1.5)
        pyautogui.click(pyautogui.locateOnScreen("D:/Uipath/SW_QC_P16/data/master/img_data/FinalShape.PNG")) # Final Shape 클릭
        time.sleep(1.5)
        pyautogui.press('down')
        time.sleep(1.5)
        pyautogui.press('down')
        time.sleep(1.5)
        pyautogui.click(pyautogui.locateOnScreen("D:/Uipath/SW_QC_P16/data/master/img_data/BoundBoxCal.PNG")) # 바운드박스 측정 클릭
        time.sleep(1.5)
        pyautogui.click(pyautogui.locateOnScreen("D:/Uipath/SW_QC_P16/data/master/img_data/Cal.PNG")) # 계산 클릭

if __name__ == '__main__':
    ModviewProcess()
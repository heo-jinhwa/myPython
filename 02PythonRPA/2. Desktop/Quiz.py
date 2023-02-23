import pyautogui
import sys
pyautogui.hotkey("win", "r") # 단축키 : win + r 입력
pyautogui.write("mspaint") # 프로그램 명 입력
pyautogui.press("enter") # 엔터키 입력

pyautogui.sleep(2) # 2초 대기

window = pyautogui.getWindowsWithTitle("그림판")[0] # 그림판 1개만 띄워져 있다고 가정
# if not window.isMaximized:
#     window.maximize() # 최대화

pyautogui.sleep(1) # 1초 대기

# 글자 버튼 클릭
btn_text = pyautogui.locateOnScreen("btn_text.png")
if btn_text:
    pyautogui.click(btn_text, duration=0.5)
else:
    print("버튼 찾기 실패")
    sys.exit()

# 브러쉬 이미지를 찾아서 상대 위치로 클릭 시도
btn_brush = pyautogui.locateOnScreen("btn_brush.png")
pyautogui.click(btn_brush.left - 200, btn_brush.top + 200)

# # 흰 영역 클릭
# pyautogui.click(200, 200, duration=0.5)

def my_write(text):
        import pyperclip
        pyperclip.copy(text) # "나도코딩" 글자를 클립보드에 저장
        pyautogui.hotkey("ctrl", "v") # 클립보드에 있는 내용 붙여넣기
my_write("참 잘했어요")

pyautogui.sleep(5) # 5초 대기

# 프로그램 종료
window.close()

# 단축키
pyautogui.sleep(0.5)
pyautogui.press("n") # 저장하지 않음

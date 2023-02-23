import pyautogui

# 자동화 프로그램 종료
# win : ctrl + alt + del 

def MouseMove():
    # 절대 좌표로 마우스 이동
    pyautogui.moveTo(100, 100) # 지정한 위치로 마우스를 이동 좌측 상단이 0, 0
    pyautogui.moveTo(200, 200, duration=1) # 1초 동안 200, 200 위치로 이동
    pyautogui.moveTo(300, 300, duration=2) # 2초 동안 300, 300 위치로 이동

    # 상대 좌표로 마우스 이동 (현재 커서가 있는 위치로부터)
    pyautogui.move(100, 100, duration=1) # 현재 위치 기준으로 +100, +100 이동
    print(pyautogui.position()) # Point(x, y)
    pyautogui.move(50, 50, duration=1) # 현재 위치 기준으로 +50, +50 이동
    print(pyautogui.position()) # Point(x, y)

    p = pyautogui.position()
    print(p[0], p[1]) # x, y
    print(p.x, p.y)

def MouseAction():
    pyautogui.sleep(3) # 3초 대기

    # # 클릭
    # pyautogui.click(64, 17, duration=1) # 1초 동안 (64, 17) 좌표로 이동 후 마우스 클릭 / pyautogui.mouseDown()+pyautogui.mouseUp() 랑 똑같음
    # # Drag & Drop에 활용 가능
    # pyautogui.mouseDown() 
    # pyautogui.mouseUp()

    # # 더블클릭
    # pyautogui.doubleClick() 
    # pyautogui.click(clicks=2)
    # pyautogui.moveTo(300, 300)
    # pyautogui.mouseDown() # 마우스 버튼 눌린 상태
    # pyautogui.moveTo(500, 500, duration=1)
    # pyautogui.mouseUp() # 마우스 버튼 떼기
    # pyautogui.rightClick() # 오른쪽 클릭
    # pyautogui.middleClick() # 휠 클릭
    
    # pyautogui.moveTo(602, 223)
    # pyautogui.drag(300, 0, duration=0.5) # 현재 위치 기준으로 100, 0 만큼 드래그 (너무 빠른 동작으로 드래그 수행 안될때 duration 사용)
    pyautogui.dragTo(1000, 223, duration=0.5) # 절대 좌표 기준으로 x 1000, y 223으로 드래그

    pyautogui.scroll(300) # 양수이면 위 방향으로, 음수이면 아래 방향으로 300만큼 스크롤 

def MouseInfo():
    # 마우스를 화면 상단모서리로 옮기면 동작 멈춤
    # pyautogui.FAILSAFE = False # 마우스를 홤녀 상단모서리로 옮겨도 동작 멈추지 않음
    # pyautogui.PAUSE = 1 # 모든 동작에 1초씩 slee 적용
    # pyautogui.mouseInfo() # 마우스 위치/색 확인가능
    for _ in range(5):
        pyautogui.move(100, 100)

def Screen():
    # 스크린 샷 찍기
    img = pyautogui.screenshot()
    img.save("screenshot.png") # 파일로 저장

    pyautogui.pixel(28, 18)
    print(pyautogui.pixelMatchesColor(28, 18, (34,167,242))) # 해당 픽셀에 RGB값이랑 비교해서 bool 값으로 반환

def ImageRecognition():
    # file_menu = pyautogui.locateOnScreen("file_menu.png")
    # print(file_menu)
    # pyautogui.click(file_menu, duration=0.25)

    # trash_menu = pyautogui.locateOnScreen("trash.png")
    # print(trash_menu)
    # pyautogui.click(trash_menu, duration=0.25)

    # screen = pyautogui.locateOnScreen("screenshot.png") # 처음 발견되는 1개 이미지만 찾음
    # print(screen)
    # pyautogui.click(screen, duration=0.25)

    # for i in pyautogui.locateAllOnScreen("checkbox.png"): # 2개 이상이 될 수 있는 이미지를 모두 찾음
    #     print(i)
    #     pyautogui.click(i, duration=0.25)

    # # 속도 개선
    # # 1. GraySacle
    # trash_menu = pyautogui.locateOnScreen("trash.png", grayscale=True) # 흑백으로 전환해서 속도 개선
    # pyautogui.moveTo(trash_menu)
    # # 2. 범위 지정
    # trash_menu = pyautogui.locateOnScreen("trash.png", region=(1488, 623, 1881-1488, 137)) 
    # pyautogui.moveTo(trash_menu)
    # # 3. 정확도 조정
    # run_btn = pyautogui.locateOnScreen("run_btn.png", confidence=0.9) # 90% 정확도로 찾기
    # pyautogui.moveTo(run_btn)
    
    # # 자동화 대상이 바로 보여지지 않는 경우
    # # 1. 계속 기다리기
    # file_menu_notepad = pyautogui.locateOnScreen("file_note.png")
    # while file_menu_notepad is None:
    #     file_menu_notepad = pyautogui.locateOnScreen("file_note.png")
    #     print("발견실패")
    # 2. 일정 시간동안 기다리기 (TimeOut)
    def find_target(img_file, timeout=30):
        import time
        start = time.time()
        target = None
        while target is None:
            target = pyautogui.locateOnScreen(img_file)
            end = time.time()
            if end - start > timeout:
                break
        return target
    
    def my_Click(img_file, timeout=30):
        import sys
        target = find_target(img_file, timeout)
        if target:
            pyautogui.click(target)
        else:
            print(f"[TimeOut {timeout}s] Target not found ({img_file}). Terminate program.")
            sys.exit()

    my_Click("file_note.png", 10)

def Window():
    # fw = pyautogui.getActiveWindow() # 현재 활성화된 창 (VSCode)
    # print(fw.title) # 창의 제목 정보
    # print(fw.size) # 창의 크기 정보 (width, height)
    # print(fw.left, fw.right, fw.top, fw.bottom) # 창의 좌표 정보
    # pyautogui.click(fw.left+25, fw.top+20)
    # for w in pyautogui.getAllWindows():
    #     print(w) # 모든 윈도우 가져오기
    w = pyautogui.getWindowsWithTitle("제목 없음")[0]
    print(w) 
    if not w.isActive:        
        w.activate() # 활성화(맨 앞으로 가져오기)
    
    if not w.isMaximized:
        w.maximize() # 최대화
    
    # if not w.isMinimized:
    #     w.minimize() # 최소화
    w.restore() # 화면 원복
    w.close() # 왼도우 닫기

def Keyboard():
    w = pyautogui.getWindowsWithTitle("제목 없음")[0] 
    w.activate()
    # 숫자/영어만 가능
    pyautogui.write("12345")
    pyautogui.write("NadoCoding", interval=0.25)

    # test순서대로 적고 왼쪽 방향키 2번, 오른쪽 방향키 1번 la 순서대로 적고 enter
    pyautogui.write(["t", "e", "s", "t", "left", "right", "l", "a", "enter"], interval=0.25)
    
    # # 특수문자
    # # shift 4 -> $
    # pyautogui.keyDown("shift") # shift 키를 누른 상태에서
    # pyautogui.press("4") # 숫자 4를 입력하고
    # pyautogui.keyUp("shift") # shift 키를 뗀다

    # # 조합키 (Hot Key)
    # pyautogui.keyDown("ctrl")
    # pyautogui.keyDown("a")
    # pyautogui.keyUp("a") # prss("A")
    # pyautogui.keyUp("ctrl") # Ctrl+A

    # # 간편한 조합키
    # pyautogui.hotkey("ctrl", "alt", "shift", "a") # 순서대로 눌렀다가 뗀다 -> Stack 형식

    def my_write(text):
        import pyperclip
        pyperclip.copy(text) # "나도코딩" 글자를 클립보드에 저장
        pyautogui.hotkey("ctrl", "v") # 클립보드에 있는 내용 붙여넣기
    my_write("나도코딩")

def MessageBox():
    pyautogui.alert("자동화 수행에 실패하였습니다.", "경고") # 확인 버튼만 있는 작업
    result = pyautogui.confirm("계속 진행하시곗습니까?", "확인") # 확인, 취소 버튼
    print(result)
    result = pyautogui.prompt("파일명을 무엇으로 하시겠습니까?", "입력") # 사용자 입력
    print(result)
    result = pyautogui.password("암호를 입력하세요.") # 패스워드
    print(result)

def Log():
    import logging
    from datetime import datetime
    # logging.basicConfig(level=logging.ERROR, format="%(asctime)s [%(levelname)s] %(message)s") # ERROR 이상 확인

    # # debug < info < warning < error < critical
    # logging.debug("아 이거 누가짯누")
    # logging.info("자동화 수행 준비")
    # logging.warning("조심조심")
    # logging.error("에러발생")
    # logging.critical("심각한 문제임")

    # # 터미널과 함께 파일에 함께 로그 남기기
    logFormatter = logging.basicConfig(level=logging.ERROR, format="%(asctime)s [%(levelname)s] %(message)s") # ERROR 이상 확인
    logger = logging.getLogger()
    # 로그 레벨 설정
    logger.setLevel(logging.DEBUG)

    # 스트림
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(logFormatter)
    logger.addHandler(streamHandler)

    # 파일
    filename = datetime.now().strftime("mylogfile_%Y%m%d%H%M%S.log") # mylogfile_20221117.log
    fileHandler = logging.FileHandler(filename, encoding="utf-8")
    fileHandler.setFormatter(logFormatter)
    logger.addHandler(fileHandler)

    logger.debug("로그를 남겨보는 테스트를 진행합니다.")

def FileSystem():
    import os
    # # 파일 기본
    # print(os.getcwd()) # current working directory 현재 작업 공간
    # os.chdir("../1. Excel")
    # print(os.getcwd())
    # os.chdir("../..") # 조부모 폴더로 이동
    # print(os.getcwd())
    # os.chdir("c:/") # 주어진 절대 경로로 이동
    # print(os.getcwd())

    # # 파일경로
    # filepath = os.path.join(os.getcwd(), "my_file.txt") # 절대 경로 생성
    # print(filepath)

    # # 전체 파일 경로에서 폴더 정보 가져오기
    # print(os.path.dirname(r"D:\★ 업무 ★\9. RPA\00. 소스\UiPath_Python\SW_Framework\Python_Script\PythonRPA\2. Desktop\my_file.txt"))

    # # 파일 정보 가져오기
    # import time
    # import datetime
    # file_path = "Desktop.py"
    # # 파일 생성 날짜
    # ctime = os.path.getctime(file_path)
    # # 날짜 정보 가져 strftime을 통해서 연원일 시분초 형태로 출력
    # print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))

    # # 파일의 수정 날짜
    # mtime = os.path.getmtime(file_path)
    # print(datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d %H:%M:%S"))

    # # 파일의 마지막 접근 날짜
    # atime = os.path.getatime(file_path)
    # print(datetime.datetime.fromtimestamp(atime).strftime("%Y%m%d %H:%M:%S"))

    # # 파일 크기
    # size = os.path.getsize(file_path)
    # print(size) # 바이트 단위로 파일 크기 가져오기

    # # 파일 목록 가져오기
    # print(os.listdir()) # 모든 폴더, 파일 목록 가져오기
    # print(os.listdir("..")) # 주어진 폴더 밑에서 모든 폴더, 파일 목록 가져오기

    # # 파일 목록 가져오기 (하위 폴더 모두 포함)
    # result = os.walk("..") # 주어진 폴더 밑에 있는 모든 폴더, 파일 목록 가져오기
    # for root, dirs, files in result:
    #     print(root, dirs, files)
    
    # # 폴더 내에서 특정 파일들을 찾으려면?
    # name = "Desk"
    # result = []
    # for root, dirs, files in os.walk("."):
    #     print(root, files)
    #     if name in files:
    #         result.append(os.path.join(root, name))
    # print(result)

    # # 폴더 내에서 특정 패턴을 가진 파일들을 찾으려면?
    # # *.xlsx, *.txt, ..
    # import fnmatch
    # pattern = "*.py" # .py로 끝나는 모든 파일
    # for root, dirs, files in os.walk("."):
    #     for name in files:
    #         if fnmatch.fnmatch(name, pattern): # 이름이 패턴과 일치하면
    #             result.append(os.path.join(root, name))
    # print(result)

    # # 주어진 경로가 파일인지, 경로인지?
    # print(os.path.isdir("2. Desktop"))
    # print(os.path.isfile("2. Desktop"))
    # print(os.path.isdir("checkbox.png"))
    # print(os.path.isfile("checkbox.png"))
    
    # # 주어진 경로가 존재하는가?
    # if os.path.exists("PythonRPA"):
    #     print("파일이 존재")
    # else:
    #     print("파일존재 안함")

    # # 파일 만들기
    # open("new_file.txt" , "a").close() # 빈 파일 생성

    # # 파일명 변경
    # os.rename("new_file.txt", "new_file_rename.txt")
    
    # # 파일 삭제하기
    # os.remove("new_file_rename.txt")

    # # 폴더 만들기
    # os.mkdir("new_folder") # 현재 경로 기준으로 폴더 생성
    # os.makedirs("new_folders/a/b/c") #

    # # 폴더명 바꾸기
    # os.rename("new_folder", "new_folder_rename")

    # # 폴더 지우기
    # os.rmdir("new_folder_rename") # 폴더 안이 비었을때만 삭제 가능

    import shutil
    # # 특정 폴더 하위 모든 파일을 삭제
    # shutil.rmtree("new_folder_rename") # 폴더 안이 비어 있지 않도록 완전 삭제가능

    # # 파일 복사하기
    # # 어떤 파일을 폴더 안으로 복사하기
    # shutil.copy("run_btn.png", "test_folder") # 원본 경로, 대상 경로
    # shutil.copy("run_btn.png", "test_folder/copied_run_btn.png") # 원본 경로, 대상 경로(파일명까지)
    # shutil.copyfile("run_btn.png", "test_folder/copied_run_btn_2.png") # 원본 파일 경로, 대상 파일 경로까지 반드시 써줘야함

    # shutil.copy2("run_btn.png", "test_folder/copy2.png")

    # # copy, copyfile : 메타정보 복사
    # # cop2 : 메타정보 복사

    # # 폴더 복사
    # shutil.copytree("test_folder", "test_folder2") # 원본 폴더 경로, 대상 폴더 경로
    
    # 폴더 이동
    # shutil.move("test_folder2" ,"test_folder3")
    





if __name__ == '__main__':
    size = pyautogui.size() # 현재 화면의 스크린 사이즈를 가져옴
    print(size) # 가로, 세로 크기를 알 수 있음 -> size[0] = width / size[1] = height
    print("현재 마우스 위치 : ", pyautogui.position())

    # MouseMove() # 1번 
    # MouseAction() # 2번
    # MouseInfo() # 3번
    # Screen() # 4번
    # ImageRecognition() # 5번
    # Window() # 6번
    # Keyboard() # 7번
    # MessageBox() # 8번
    # Log() # 9번
    FileSystem() # 10번

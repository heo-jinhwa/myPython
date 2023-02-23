import cv2
import numpy as np

# 1. 이미지 변형 (흑백) - 전처리
def BlackWhite():
    # img = cv2.imread('./data/img.jpg', cv2.IMREAD_GRAYSCALE) # 흑백으로 이미지 불러오기
    img = cv2.imread('./data/img.jpg')
    dst = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 불러온 이미지를 흑백으로 변환

    cv2.imshow('img', img)
    cv2.imshow('Gray', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 2. 이미지 변형 (흐림) - 가우시안 블러 : 커널 사이즈 변화에 따른 흐림
def blur_kernel():
    img = cv2.imread('./data/img.jpg')
    # kernel size : [3, 3], [5, 5], [7, 7]
    kernel_3 = cv2.GaussianBlur(img, [3, 3], 0)
    kernel_5 = cv2.GaussianBlur(img, [5, 5], 0)
    kernel_7 = cv2.GaussianBlur(img, [7, 7], 0)

    cv2.imshow('img', img)
    cv2.imshow('kernel_3', kernel_3)
    cv2.imshow('kernel_5', kernel_5)
    cv2.imshow('kernel_7', kernel_7) # 더 흐린 효과 
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 3. 이미지 변형 (흐림) - 표준 편차 변화에 따른 흐림
def blur_std():
    img = cv2.imread('./data/img.jpg')
    
    sigma_1 = cv2.GaussianBlur(img, [0, 0], 1) # sigmaX - 가우시안 커널의 X방향의 표준 편차
    sigma_2 = cv2.GaussianBlur(img, [0, 0], 2)
    sigma_3 = cv2.GaussianBlur(img, [0, 0], 3)

    cv2.imshow('img', img)
    cv2.imshow('sigma_1', sigma_1)
    cv2.imshow('sigma_2', sigma_2)
    cv2.imshow('sigma_3', sigma_3) # 더 흐린 효과 
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 4. 이미지 변형 (원근) : 사다리꼴 이미지 펼치기
def perspective1():
    img = cv2.imread('./data/newpaper.jpg')
    
    width, height = 640, 240 # 가로 640, 세로 240으로 결과물 출력
    
    src = np.array([[511, 352], [1008, 345], [1122, 584], [455,594]], dtype=np.float32) #input 4개 점 (왼쪽 상단 점부터 시계방향으로 4개)
    dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)
    # 좌상, 우상, 우하, 좌하 (시계 방향으로 4지점 정의)

    matrix = cv2.getPerspectiveTransform(src, dst) # Matrix를 얻어옴 (src영역 -> dst영역)
    result = cv2.warpPerspective(img, matrix, (width, height)) # matrix대로 변환

    cv2.imshow('img', img)
    cv2.imshow('result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 4. 이미지 변형 (원근) : 회전된 이미지 올바로 세우기
def perspective2():
    img = cv2.imread('./data/poker.jpg')
    
    width, height = 530, 710
    
    src = np.array([[702, 143], [1133, 414], [726, 1007], [276, 700]], dtype=np.float32) #input 4개 점 (왼쪽 상단 점부터 시계방향으로 4개)
    dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)
    # 좌상, 우상, 우하, 좌하 (시계 방향으로 4지점 정의)

    matrix = cv2.getPerspectiveTransform(src, dst) # Matrix를 얻어옴 (src영역 -> dst영역)
    result = cv2.warpPerspective(img, matrix, (width, height)) # matrix대로 변환

    cv2.imshow('img', img)
    cv2.imshow('result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 미니 프로젝트 : 반자동 문서 스캐너
def mouse_handler(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN: # 마우스 왼쪽버튼
        print('왼쪽 버튼 Down')
    elif event == cv2.EVENT_LBUTTONUP: # 마우스 왼쪽 버튼 UP
        print('왼쪽 버튼 UP')
    elif event == cv2.EVENT_LBUTTONDBLCLK: # 마우스 왼쪽 버튼 더블 클릭
        print('왼쪽 버튼 Double Click')
    elif event == cv2.EVENT_RBUTTONDOWN: # 오른쪽 마우스 다운
        print('오른쪽 버튼 Down')
    elif event == cv2.EVENT_RBUTTONUP: # 오른쪽 마우스 UP
        print('오른쪽 버튼 UP')
    elif event == cv2.EVENT_RBUTTONDBLCLK: # 오른쪽 마우스 더블 클릭
        print('오른쪽 버튼 Double Click')
    # elif event == cv2.EVENT_MOUSEMOVE: # 마우스 이동
    #     print('마우스 이동')

def MiniProject():
    src_img = cv2.imread('./data/poker.jpg')
    cv2.namedWindow('img window') # img 이름으로 윈도우창  만들기, 여기에 마우스 이벤트를 처리하기 위한 핸들러 적용
    cv2.setMouseCallback('img window', mouse_handler)
    cv2.imshow('img window', src_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # BlackWhite()
    # blur_kernel()
    # blur_std()
    # perspective1()
    # perspective2()
    MiniProject()
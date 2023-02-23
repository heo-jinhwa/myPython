import cv2
import numpy as np

# 1. 빈 스케치북 만들기
def Create_Sketch():
    # 세로 480 X 가로 640, 3Channel (RGB)에 해당하는 스케치북 만들기
    img = np.zeros((480, 640, 3), dtype=np.uint8)
    # img[:] = (255, 255, 255) # 전체 공간을 흰 색으로 만들기
    # print(img)
    cv2.imshow('img-title', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 2. 일부 영역 색칠
def Create_Part():
    img = np.zeros((480, 640, 3), dtype=np.uint8)
    img[100:200, 200:300] = (255, 255, 255) # 세로 영역, 가로 영역 흰색으로 채우기
    cv2.imshow('img-title', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 3. 직선 그리기
def Create_Line():
    # cv2.LINE_4 : 상하좌우 4 방향으로 연결된 선
    # cv2.LINE_8 : 대각선을 포함한 8 방향으로 연결된 선 (기본값)
    # cv2.LINE_AA : 부드러운 선 (anti-aliasing)
    img = np.zeros((480, 640, 3), dtype=np.uint8)
    COLOR = (0, 255, 255) # BGR : Yellow 색깔
    THICKNESS = 3 # 두께 
    cv2.line(img, (50, 100), (400, 50), COLOR, THICKNESS, cv2.LINE_8) # 두 점을 직선으로 연결
    # 선을 그릴 그림, 시작 점, 끝 점, 색깔, 두께, 선 종류
    cv2.line(img, (50, 200), (400, 150), COLOR, THICKNESS, cv2.LINE_4) 
    cv2.line(img, (50, 300), (400, 250), COLOR, THICKNESS, cv2.LINE_AA) 

    cv2.imshow('img-title', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 4. 원 그리기
def Create_Circle():
    img = np.zeros((480, 640, 3), dtype=np.uint8)
    COLOR = (255, 255, 0) # BGR
    RADIUS = 50 # 반지름
    THICKNESS = 10 # 두께 

    cv2.circle(img, center=(200, 100), radius=RADIUS, color=COLOR, thickness=THICKNESS, lineType=cv2.LINE_AA)
    # 원을 그릴 그림, 중심점, 반지름, 색깔, 두께, 선 종류

    cv2.circle(img, (400, 100), RADIUS, COLOR, cv2.FILLED, cv2.LINE_AA)

    cv2.imshow('img-title', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 5. 다각형
def Create_Star():
    img = np.zeros((480, 640, 3), dtype=np.uint8)
    COLOR = (0, 0, 255) # BGR
    THICKNESS = 3 # 두께 

    pts1 = np.array([[100, 100], [200, 100], [100, 200]]) # 3개의 점을 순차적으로 연결
    pts2 = np.array([[200, 100], [300, 100], [300, 200]])
    cv2.polylines(img, [pts1], True, COLOR, THICKNESS, cv2.LINE_AA) # 마지막 점과 첫 점을 연결하여 닫힌 도형으로 만든다
    cv2.polylines(img, [pts2], True, COLOR, THICKNESS, cv2.LINE_AA) # 마지막 점과 첫 점을 연결하여 닫힌 도형으로 만든다
    cv2.polylines(img, [pts1, pts2], True, COLOR, THICKNESS, cv2.LINE_AA) # 속이 비어있는 다각형
    # 그릴 img 위치, 그릴 좌표들, 닫힘 여부, 색깔, 두께, 선 종류
    
    pts3 = np.array([[[100, 300], [200, 300], [100, 400]], [[200, 300], [300, 300], [300, 400]]])
    cv2.fillPoly(img, pts3, COLOR, cv2.LINE_AA)
    # 그릴 img 위치, 그릴 좌표들, 색깔, 선 종류

    cv2.imshow('img-title', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    # Create_Star()
    Create_Circle()
import cv2
import numpy as np

# 1. 윤곽선 검출 - 이미지 검출
# 2. 윤곽선 찾기 모드
# cv2.RETR_EXTERNAL : 가장 외곽의 윤곽선만 찾음
# cv2.RETR_LIST : 모든 윤곽선을 찾음 (계층 정보 없음)
# cv2.RETR_TREE : 모든 윤곽선을 찾음 (계층 정보를 트리 구조로 생성)

def Contour(mode):
    img = cv2.imread('./data/img.jpg')
    target_img = img.copy() # 사본 이미지 ★ 윤곽선을 위해 binary 처리 필요함 ★
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    contours, hierarchy = cv2.findContours(otsu, mode, cv2.CHAIN_APPROX_NONE)
    # 윤곽선 정보와 구조 반환 / 이미지, 윤곽선 찾는 mode, 윤곽선 찾는 근사치 방법(method) : CHAIN_APPOX_NONE, CHAIN_APPOX_SIMPLE
    print(hierarchy)
    print('총 발견 개수 {}'.format(len(contours)))

    COLOR = (0, 200, 2) # 녹색
    cv2.drawContours(target_img, contours, -1, COLOR, 2) # 이미지에 윤곽선 그리기
    # 이미지, 윤곽선 정보, 인덱스(-1이면 전체), 색깔, 두께
    
    cv2.imshow('img', img)
    cv2.imshow('gray', gray)
    cv2.imshow('otsu', otsu) # 이진화 그림
    cv2.imshow('contour', target_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 경계 사각형 : 윤곽선의 경계면을 둘러싸는 사각형
def ContourRec(mode):
    img = cv2.imread('./data/img.jpg')
    target_img = img.copy() # 사본 이미지 ★ 윤곽선을 위해 binary 처리 필요함 ★
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    contours, hierarchy = cv2.findContours(otsu, mode, cv2.CHAIN_APPROX_NONE)
    # 윤곽선 정보와 구조 반환 / 이미지, 윤곽선 찾는 mode, 윤곽선 찾는 근사치 방법(method)
    print(hierarchy)
    print('총 발견 개수 {}'.format(len(contours)))

    COLOR = (0, 200, 2) # 녹색
    for cnt in contours:
        x, y, width, height = cv2.boundingRect(cnt)
        cv2.rectangle(target_img, (x, y), (x+width, y+height), color=COLOR, thickness=2)

    cv2.imshow('img', img)
    cv2.imshow('contour', target_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 면적 구하기
def ContourArea(mode):
    img = cv2.imread('./data/img.jpg')
    img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    target_img = img.copy() # 사본 이미지 ★ 윤곽선을 위해 binary 처리 필요함 ★
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    contours, hierarchy = cv2.findContours(otsu, mode, cv2.CHAIN_APPROX_NONE)
    # 윤곽선 정보와 구조 반환 / 이미지, 윤곽선 찾는 mode, 윤곽선 찾는 근사치 방법(method)
    print(hierarchy[0][:5])
    print('총 발견 개수 {}'.format(len(contours)))

    COLOR = (0, 200, 2) # 녹색
    for idx, cnt in enumerate(contours):
        if cv2.contourArea(cnt):
            x, y, width, height = cv2.boundingRect(cnt)
            cv2.rectangle(target_img, (x, y), (x+width, y+height), color=COLOR, thickness=2)
            cv2.circle(target_img, (x, y), 5, (255, 255, 0), cv2.FILLED, cv2.LINE_AA) # 중심점 그리기

    cv2.imshow('img', img)
    cv2.imshow('contour', target_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    # 3가지 모드에 따라서 윤곽선 찾기
    for mode in [cv2.RETR_EXTERNAL, cv2.RETR_LIST, cv2.RETR_TREE]:
        ContourArea(mode)
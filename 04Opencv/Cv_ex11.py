import cv2
import numpy as np
# 이진화 알고리즘 -> 윤곽선 검출을 위해서 필요한 과정

# 1. Threshold 
def Binary_image():
    img = cv2.imread('./data/book.jpg', cv2.IMREAD_GRAYSCALE)

    ret, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) # 픽셀이 127보다 크면 255값으로 바꾼다 (흰색으로 변경)
    cv2.imshow('img', img)
    cv2.imshow('binary', binary)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 2. Trackbar (값 변화에 따른 변형 확인)
def empty(pos):
    print(pos)
    pass

def Trackbar_image():
    img = cv2.imread('./data/book.jpg', cv2.IMREAD_GRAYSCALE)
    
    window_name = 'Trackbar'
    bar_name = 'threshold'
    cv2.namedWindow(window_name)

    cv2.createTrackbar(bar_name, window_name, 127, 255, empty) # bar 이름, 창의 이름, 초기값, 최대값, 이벤트 처리
    
    while True:
        thresh = cv2.getTrackbarPos(bar_name, window_name) # bar 이름, 창의 이름
        ret, binary = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)
        if not ret:
            break
        cv2.imshow(window_name, binary)
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()

# 3. Adaptive Threshold
# 이미지를 작은 영역으로 나누어서 임계치 적용
def AdaptiveThreshod():
    img = cv2.imread('./data/book.jpg', cv2.IMREAD_GRAYSCALE)
    
    window_name = 'Trackbar'
    
    cv2.namedWindow(window_name)

    cv2.createTrackbar('block_size', window_name, 25, 100, empty) # block_size : 홀수만 가능, 1보다는 큰 값
    cv2.createTrackbar('c', window_name, 3, 10, empty) # c : 일반적으로 양수의 값을 사용

    while True:
        block_size = cv2.getTrackbarPos('block_size', window_name) # bar 이름, 창의 이름
        c = cv2.getTrackbarPos('c', window_name) # bar 이름, 창의 이름

        if block_size <= 1: # 1 이하면 3으로 변경
            block_size = 3
        if block_size % 2 == 0: # 짝수이면 홀수로 변경
            block_size += 1

        binary = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, c)
        
        cv2.imshow(window_name, binary)
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()

# 오츠 알고리즘 : Bimodal Image에 사용하기 적합 (최적의 임계치를 자동으로 발견)
def Otsu():
    img = cv2.imread('./data/book.jpg', cv2.IMREAD_GRAYSCALE)

    ret, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    ret, otsu = cv2.threshold(img, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    print('otsu threshold : ', ret)

    cv2.imshow('img', img)
    cv2.imshow('binary', binary)
    cv2.imshow('otsu', otsu)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    # Trackbar_image()
    # AdaptiveThreshod()
    Otsu()
import cv2
import numpy as np
# 이미지 변환 (팽창, 침식)

# 1. 팽창 (이미지를 확장하여 작은 구멍을 채움 -> )
def Dilate():
    kernel = np.ones((3, 3), np.uint8)

    img = cv2.imread('./data/dilate.png', cv2.IMREAD_GRAYSCALE)
    dilate1 = cv2.dilate(img, kernel, iterations=1) # 반복횟수 1회
    dilate2 = cv2.dilate(img, kernel, iterations=2) # 반복횟수 2회
    dilate3 = cv2.dilate(img, kernel, iterations=3) # 반복횟수 3회
    
    cv2.imshow('gray', img)
    cv2.imshow('dilate1', dilate1)
    cv2.imshow('dilate2', dilate2)
    cv2.imshow('dilate3', dilate3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 2. 침식 (이미지를 깎는 과정)
def Erode():
    kernel = np.ones((3, 3), np.uint8)

    img = cv2.imread('./data/erode.png', cv2.IMREAD_GRAYSCALE)
    erode1 = cv2.erode(img, kernel, iterations=1) # 반복횟수 1회
    erode2 = cv2.erode(img, kernel, iterations=2) # 반복횟수 2회
    erode3 = cv2.erode(img, kernel, iterations=3) # 반복횟수 3회
    
    cv2.imshow('gray', img)
    cv2.imshow('erode1', erode1)
    cv2.imshow('erode2', erode2)
    cv2.imshow('erode3', erode3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    Erode()

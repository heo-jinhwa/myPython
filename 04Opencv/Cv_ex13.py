import cv2
import numpy as np
# 이미지 변환 (열림, 닫힘)

# 1. 열림 (침식 후 팽창, 깎아샤ㅓ 노이즈 제거후 살 찌움)
def Opening():
    kernel = np.ones((3, 3), dtype=np.uint8)

    img = cv2.imread('./data/erode.png', cv2.IMREAD_GRAYSCALE)
    erode = cv2.erode(img, kernel, iterations=3)
    dilate = cv2.dilate(erode, kernel, iterations=3)

    cv2.imshow('gray', img)
    cv2.imshow('erode', erode)
    cv2.imshow('dilate', dilate)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 2. 닫힘 (팽창 후 침식, 구멍을 메운 후 다시 깎음)
def Closing():
    kernel = np.ones((3, 3), dtype=np.uint8)

    img = cv2.imread('./data/dilate.png', cv2.IMREAD_GRAYSCALE)
    dilate = cv2.dilate(img, kernel, iterations=3)
    erode = cv2.erode(dilate, kernel, iterations=3)

    cv2.imshow('gray', img)
    cv2.imshow('dilate', dilate)
    cv2.imshow('erode', erode)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    Closing()
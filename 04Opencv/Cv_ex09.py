import cv2
import numpy as np

# 이미지 회전

# 1. 시계방향 90도 회전
def Rotate90():
    img = cv2.imread('./data/img.jpg')
    
    Rotate_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) # 시계 방향으로 90도 회전
    
    cv2.imshow('img', img)
    cv2.imshow('Rotate_90', Rotate_90)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 2. 180도 회전
def Rotate180():
    img = cv2.imread('./data/img.jpg')
    
    Rotate_180 = cv2.rotate(img, cv2.ROTATE_180) # 180도 회전
    
    cv2.imshow('img', img)
    cv2.imshow('Rotate_180', Rotate_180)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 3. 시계 반대 방향 90도 회전 (시계 방향 270도 회전)
def Rotate90R():
    img = cv2.imread('./data/img.jpg')
    
    Rotate_180R = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE) # 시계 반대 방향으로 90도 회전
    
    cv2.imshow('img', img)
    cv2.imshow('Rotate_180R', Rotate_180R)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    Rotate90()
    Rotate180()
    Rotate90R()
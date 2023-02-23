import cv2
import numpy as np

# 이미지 대칭

# 1. 좌우대칭
def LR_Symmetry():
    img = cv2.imread('./data/img.jpg')
    flip_horizontal = cv2.flip(img, 1) # filpcode > 0 : 좌우 대칭 Horizontal
    
    cv2.imshow('img', img)
    cv2.imshow('filp_horizontal', flip_horizontal)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 2. 상하대칭
def TB_Symmetry():
    img = cv2.imread('./data/img.jpg')
    flip_vertical = cv2.flip(img, 0) # filpcode = 0 : 상하 대칭 Vertical
    
    cv2.imshow('img', img)
    cv2.imshow('flip_vertical', flip_vertical)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 3. 상하좌우
def TBLR_Symmetry():
    img = cv2.imread('./data/img.jpg')
    flip_both = cv2.flip(img, -1) # filpcode < 0 : 상하좌우 대칭 Both
    
    cv2.imshow('img', img)
    cv2.imshow('flip_both', flip_both)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    LR_Symmetry()
    TB_Symmetry()
    TBLR_Symmetry()
import cv2
import numpy as np

# 영역을 잘라서 새로운 윈도우(창)에 표시

# 1. 크기 조정 (고정 크기로 설정)
def Cut_Part():
    img = cv2.imread('./data/img.jpg')
    # img.shape # (640, 613, 3)

    crop = img[100:200, 200:400] # 세로 기준 100~200 / 가로 기준 200~400까지 자름

    cv2.imshow('img', img)
    cv2.imshow('crop_img', crop)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 2. 영역을 잘라서 기존 윈도우에 표시
def Cut_Part2():
    img = cv2.imread('./data/img.jpg')

    crop = img[100:200, 200:400] # 세로 기준 100~200 / 가로 기준 200~400까지 자름
    img[100:200, 400:600] = crop # 세로 기준 100~200 / 가로 기준 400~600까지 위 crop 이미지를 넣어줌
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    Cut_Part2()
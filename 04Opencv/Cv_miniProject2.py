import cv2
import numpy as np

# 카드 검출 & 분류기 프로젝트

def ContourArea(mode):
    img = cv2.imread('./data/card.png')
    target_img = img.copy() # 사본 이미지 ★ 윤곽선을 위해 binary 처리 필요함 ★
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    contours, hierarchy = cv2.findContours(otsu, mode, cv2.CHAIN_APPROX_NONE) # 윤곽선 정보와 구조 반환 / 이미지, 윤곽선 찾는 mode, 윤곽선 찾는 근사치 방법(method)
    
    COLOR = (0, 200, 2) # 녹색
    idx = 1
    for cnt in contours:
        if cv2.contourArea(cnt) > 25000:
            x, y, width, height = cv2.boundingRect(cnt)
            cv2.rectangle(target_img, (x, y), (x+width, y+height), color=COLOR, thickness=2)

            crop = img[y:y+height, x:x+width] # 사각형 영역만큼 짜르기
            cv2.imshow('card_crop{}'.format(idx), crop)
            cv2.imwrite('./data/card_crop{}.png'.format(idx), crop)
            idx += 1

    cv2.imshow('img', img)
    cv2.imshow('contour', target_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    # 3가지 모드에 따라서 윤곽선 찾기
    for mode in [cv2.RETR_LIST]:
        ContourArea(mode)
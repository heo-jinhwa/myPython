import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image # 한글 우회 Library (PIL : Python Image Library)

# 한글로 쓸 함수
def myPutText(src, text, pos, font_size, font_color):
    img_pil = Image.fromarray(src)
    draw = ImageDraw.Draw(img_pil)
    font = ImageFont.truetype('font/gulim.ttc', font_size)
    draw.text(pos, text, font=font, fill=font_color)
    return np.array(img_pil)

# OpenCV에서 사용하는 글꼴 종류
# 1. cv2.FONT_HERSHEY_SIMPLEX : 보통 크기의 산 세리프(sans-serif) 글꼴
# 2. cv2.FONT_HERSHEY_PLAIN : 작은 크기의 산 세리프 글꼴
# 3. cv2.FONT_HERSHEY_SCRIPT_SIMPLEX : 필기체 스타일 글꼴
# 4. cv2.FONT_HERSHEY_TRIPLEX : 보통 크기의 산 세리프 글꼴
# 5. cv2.FONT_ITALIC : 기울임 (이탤릭체)

# 1. 기본 텍스트 쓰기
def PutText():
    # 세로 480 X 가로 640, 3Channel (RGB)에 해당하는 스케치북 만들기
    img = np.zeros((480, 640, 3), dtype=np.uint8)
    SCALE = 1
    COLOR = (255, 255, 255) # 흰색
    THICKNESS = 1

    # 그릴 위치, 텍스트 내용, 시작 위치, 폰트 종류, 크기, 색깔, 두께
    cv2.putText(img, "Hjina Simplex", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, SCALE, COLOR, THICKNESS)
    cv2.putText(img, "Hjina PLAN", (20, 150), cv2.FONT_HERSHEY_PLAIN, SCALE, COLOR, THICKNESS)
    cv2.putText(img, "Hjina SCRIPT Simplex", (20, 250), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, SCALE, COLOR, THICKNESS)
    cv2.putText(img, "Hjina TRIPLEX", (20, 350), cv2.FONT_HERSHEY_TRIPLEX, SCALE, COLOR, THICKNESS)
    cv2.putText(img, "Hjina ITALIC", (20, 450), cv2.FONT_HERSHEY_TRIPLEX | cv2.FONT_ITALIC, SCALE, COLOR, THICKNESS)

    cv2.imshow('img-title', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 2. 한글 텍스트 쓰기
def PutText_Korean():
    # 세로 480 X 가로 640, 3Channel (RGB)에 해당하는 스케치북 만들기
    img = np.zeros((480, 640, 3), dtype=np.uint8)
    FONT_SIZE = 30
    COLOR = (255, 255, 255) # 흰색

    # 그릴 위치, 텍스트 내용, 시작 위치, 폰트 종류, 크기, 색깔, 두께
    # cv2.putText(img, "허진화", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, SCALE, COLOR, THICKNESS)
    img = myPutText(img, "허진화", (20, 50), FONT_SIZE, COLOR)

    cv2.imshow('img-title', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    PutText()
    PutText_Korean()
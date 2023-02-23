import cv2
import numpy as np

# 이미지 크기 조정

# 1. 크기 조정 (고정 크기로 설정)
def Modify_Fixed_Size():
    img = cv2.imread('./data/img.jpg')
    dst = cv2.resize(img, (400, 500)) # width, height 고정 크기로 변환
    cv2.imshow('img', img)
    cv2.imshow('resize', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 2. 크기 조정 (비율 크기로 설정)
def Modify_Ratio_Size():
    img = cv2.imread('./data/img.jpg')
    dst = cv2.resize(img, None, fx=0.5, fy=0.5) # x, y 비율 정의 (0.5배 축소)
    cv2.imshow('img', img)
    cv2.imshow('resize', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 보간법
# 1. cv2.INTER_AREA : 크기 줄일 때 사용
# 2. cv2.INTER_CUBIC : 크기 늘릴 때 사용 (속도 느림, 퀄리티 좋음)
# 3. cv2.INTER_LINEAR : 크기 늘릴 때 사용 (기본 값)

# 3. 크기 축소 (보간법 적용)
def Modify_Size_Down():
    img = cv2.imread('./data/img.jpg')
    dst = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA) # x, y 비율 정의 (0.5배 축소)
    cv2.imshow('img', img)
    cv2.imshow('resize', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 4. 크기 확대 (보간법 적용)
def Modify_Size_Up():
    img = cv2.imread('./data/img.jpg')
    dst = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC) # x, y 비율 정의 (1.5배 확대)
    cv2.imshow('img', img)
    cv2.imshow('resize', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 5. 비디오 크기 조정 (고정 크기로 설정)
def Modify_Fixed_Size():
    cap = cv2.VideoCapture('./data/video.mp4')

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_resized = cv2.resize(frame, (400, 500))
        cv2.imshow('video', frame_resized)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# 6. 비디오 크기 조정 (비율 크기로 설정)
def Modify_Fixed_Size():
    cap = cv2.VideoCapture('./data/video.mp4')

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_resized = cv2.resize(frame, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
        cv2.imshow('video', frame_resized)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    Modify_Fixed_Size()
    Modify_Ratio_Size()
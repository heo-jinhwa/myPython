import cv2
import numpy as np

# 1. 파일 저장 (이미지)
def Save_Image(format):
    img = cv2.imread('./data/img.jpg', cv2.IMREAD_GRAYSCALE) # 흑백으로 이미지 불러오기

    cv2.imshow('img-title', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    if format == 'jpg':
        result = cv2.imwrite('./data/save_img.jpg', img) # 확장자는 jpg / png 상관 없음
    else:
        result = cv2.imwrite('./data/save_img.png', img) # 확장자는 jpg / png 상관 없음
    print(result)

# 2. 파일 저장 (동영상)
def Save_Video():
    cap = cv2.VideoCapture('./data/video.mp4')
    
    # 코덱정의
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')

    # 프레임 크기, fps(영상 속도) 정의
    width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS) * 2 # 영상 재생 속도 2배

    # 저장 파일명, 코덱, fps, 크기(width, height)
    out = cv2.VideoWriter('./data/output.avi', fourcc, fps, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        out.write(frame) # 영상 데이터만 저장 (소리 X)

        cv2.imshow('video', frame)
        if cv2.waitKey(1) == ord('q'):
            break

    out.release()
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    Save_Video()
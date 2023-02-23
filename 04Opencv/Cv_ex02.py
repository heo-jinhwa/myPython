import cv2

# 1. 동영상 파일 출력
def Video_Show(path):
    cap = cv2.VideoCapture(path)
    
    while cap.isOpened(): # 동영상 파일이 올바로 열렸는지 ?
        ret, frame = cap.read() # ret : 성공여부, frame : 받아온 이미지 (프레임)
        if not ret:
            print('더 이상 가져올 프레임이 없어요')
            break
        
        cv2.imshow('video', frame)
        
        if cv2.waitKey(1) == ord('q'): # 사용자가 q를 입력하면
            print('사용자 입력에 의해 종료됩니다.')
            break
    cap.release() # 자원 해제
    cv2.destroyAllWindows() # 모든 창 닫기

# 2. 카메라 출력
def Camera_Show():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) # 0번째 카메라 장치 (Device id)
    if not cap.isOpened(): # 카메라가 잘 열리지 않은 경우
        exit() # 프로그램 종료
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print('가져온 프레임이 없어요')
            break
        
        cv2.imshow('camera', frame)
        if cv2.waitKey(1) == ord('q'): # 사용자가 q를 입력하면
            print('사용자 입력에 의해 종료됩니다.')
            break
    
    cap.release() # 자원 해제
    cv2.destroyAllWindows() # 모든 창 닫기  

if __name__ == '__main__':
    # Video_Show('./data/video.mp4')
    Camera_Show()
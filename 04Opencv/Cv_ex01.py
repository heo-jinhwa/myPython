import cv2

# 다양한 영상(이미지) / 동영상 처리에 사용되는 오픈소스 라이브러리
print(cv2.__version__)

# 1. 이미지 출력
def Img_Show(path, title):
    img = cv2.imread('./data/img.jpg') # 해당 경로의 파일 읽어오기
    cv2.imshow('img-title', img) # img라는 이름의 창에 img_title를 표시
    cv2.waitKey(0) # 지정된 시간(ms) 동안 사용자 키 입력 대기
    cv2.destroyAllWindows() # 모든 창 Close

# 2. 읽기 옵션 
def Read_Options(path):
    # cv2.IMREAD_COLOR : 컬러 이미지, 투명 영역은 무시 (기본값)
    # cv2.IMREAD_GRAYSCALE : 흑백 이미지
    # cv2.IMREAD_UNCHANGED : 투명 영역까지 포함
    img_color = cv2.imread(path, cv2.IMREAD_COLOR)
    img_gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    img_unchanged = cv2.imread(path, cv2.IMREAD_UNCHANGED)

    cv2.imshow('img-color', img_color)
    cv2.imshow('img-gray', img_gray)
    cv2.imshow('img-unchanged', img_unchanged)

    cv2.waitKey(0)
    cv2.destroyAllWindows() 

# 3. Shape : 이미지의 Height, Width, Channel 정보
def Shape(path):
    img = cv2.imread(path)
    print(img.shape) # 세로 가로 Channel

if __name__ == '__main__':
    Img_Show('./data/img.jpg', 'img-title')
    # Read_Options('./data/img.jpg')
    # Shape('./data/img.jpg')


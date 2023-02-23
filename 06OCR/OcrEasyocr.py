# pip install opencv-contrib-python==4.5.4.60 
# pip install easyocr
import easyocr
import cv2
import matplotlib.pyplot as plt

def myocr(img_path):
    print("RPA S맨 : 이미지에서 텍스트 추출 작업 중입니다.")
    if ('.jpg' not in img_path.lower()) and ('.png' not in img_path.lower()): # 이미지 파일이 아닌 경우에는 바로 종료
        return ["Need to image file"] # message 반환
    r = [] # 추출된 단어를 담을 리스트
    THRESHOLD = 0.5 # 최소 정확도 기준
    reader = easyocr.Reader(['ko', 'en']) # easyocr 작업시 선택 할 언어
    img = cv2.imread(img_path) # cv2로 image 파일 read
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 회색으로 변환
    result = reader.readtext(img_gray) # img에서 text 추출 - OCR 작업
    for bbox, text, conf in result: # bbox(해당 text의 위치), text(추출된 문자), conf(정확도)
        if conf >= THRESHOLD: # conf(정확도)가 THRESHOLD 이상일 때만 리스트에 담는다.
            r.append(text) 
            cv2.rectangle(img_gray, pt1=(int(bbox[0][0]), int(bbox[0][1])), pt2=(int(bbox[2][0]), int(bbox[2][1])), color=(0, 255, 0), thickness=3) # image에 사각형 표시

    show_image(img_gray)

    return r

def show_image(img):
    cv2.imshow('result_image', img)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    print(myocr('./img_data/sample4.jpg'))

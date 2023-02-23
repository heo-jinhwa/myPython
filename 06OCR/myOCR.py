# pip install opencv-contrib-python==4.5.4.60 
# pip install easyocr
import easyocr
import cv2
import matplotlib.pyplot as plt

class myocr:
    def __init__(self, file_path, THRESHOLD):
        self._file_path = file_path
        self._img = None
        self._THRESHOLD = THRESHOLD # 최소 정확도 기준
        self._ocrReader = easyocr.Reader(['ko', 'en']) # easyocr 작업시 선택 할 언어
        self.__ocrResult = [] # 추출된 단어를 담을 리스트 (은닉)
    
    @property
    def ocrResult(self):
        return self.__ocrResult
    
    @ocrResult.setter
    def ocrResult(self, value):
        self.__ocrResult.append(value)

    # 결과를 보여주는 함수
    def show_image(self): 
        cv2.imshow('result_image', self._img)
        cv2.waitKey(2000)
        cv2.destroyAllWindows()
    
    # 이미지 전처리 함수
    def image_preprocessing(self):
        self._img = cv2.cvtColor(self._img, cv2.COLOR_BGR2GRAY) # 회색으로 변환

    # ocr 작업 프로세스 함수
    def ocr_process(self):
        print("RPA S맨 - 이미지에서 텍스트 추출 작업 진행중입니다.")
        if ('.jpg' not in self._file_path.lower()) and ('.png' not in self._file_path.lower()): # 이미지 파일이 아닌 경우 바로 종료
            return ["Need to image file"]
        
        self._img = cv2.imread(self._file_path) # cv2로 이미지파일 read
        self.image_preprocessing() # 이미지 전처리

        result = self._ocrReader.readtext(self._img)
        for bbox, text, conf in result: # bbox(해당 text의 위치), text(추출된 문자), conf(정확도)
            if conf >= self._THRESHOLD: # conf(정확도)가 THRESHOLD 이상일 때만 리스트에 담는다.
                self.ocrResult = text # Setter로 결과값 넣어주기
                cv2.rectangle(
                    self._img, 
                    pt1=(int(bbox[0][0]), int(bbox[0][1])), 
                    pt2=(int(bbox[2][0]), int(bbox[2][1])), 
                    color=(0, 255, 0), 
                    thickness=3
                ) # image에 사각형 표시

        self.show_image() # 결과 보기

if __name__ == '__main__':
    myocr_ = myocr('./img_data/sample4.jpg', 0.5)
    myocr_.ocr_process() # ocr 작업 시작
    print(myocr_.ocrResult)
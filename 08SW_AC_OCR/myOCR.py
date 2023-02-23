# pip install opencv-contrib-python==4.5.4.60 
# pip install easyocr

import easyocr
import cv2

class myocr:
    def __init__(self, file_path, THRESHOLD):
        self._file_path = file_path
        self._img = None
        self._THRESHOLD = THRESHOLD # 최소 정확도 기준
        self._center = []
        # self._ocrReader = easyocr.Reader(['ko'], model_storage_directory='./user_model', user_network_directory='./user_model', recog_network='custom') # easyocr 작업시 선택 할 언어
        self._ocrReader = easyocr.Reader(['ko']) # easyocr 작업시 선택 할 언어
        self.__ocrResult = '' # 추출된 단어를 담을 문자열 (은닉)        
    
    @property
    def ocrResult(self):
        return self.__ocrResult
    
    @ocrResult.setter
    def ocrResult(self, value):
        self.__ocrResult = self.__ocrResult + "[" + value + "] "
    
    # 이미지 읽기
    def read_image(self):
        self._img = cv2.imread(self._file_path) # cv2로 이미지파일 read
        x, y, _ = self._img.shape # image 크기
        self._center.append(int(x/2)) # 중심점 x 
        self._center.append(int(y/2)) # 중심점 y
        cv2.circle(self._img, (self._center[1], self._center[0]), 5, (255,255,0), cv2.FILLED, cv2.LINE_AA) # 중심점 그리기

    # 결과를 보여주는 함수
    def show_image(self):
        cv2.imshow('result_image', cv2.resize(self._img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA))
        cv2.waitKey()
        cv2.destroyAllWindows()
    
    # 이미지 전처리 함수
    def image_preprocessing(self):
        # 블러를 사용해서 잡음 제거 + THRESHOLDING을 통해 화면의 검은색과 흰색을 나눌 수 있음 -> 컴퓨터 인식에 용이 + findContours : 윤곽선을 찾는다(선으로) / 이진화 함수를 사용해서 0 아니면 1로 이미지를 표현하는 방법이 Threshold 함수
        # ■ RGB -> Gray
        self._img = cv2.cvtColor(self._img, cv2.COLOR_BGR2GRAY) 
        # ret, self._img = cv2.threshold(self._img, 230, 255, cv2.THRESH_BINARY)

    # ocr 작업 프로세스 함수
    def ocr_process(self):
        print("RPA S맨 : 이미지에서 텍스트 추출 작업 진행중입니다.")
        if ('.jpg' not in self._file_path.lower()) and ('.png' not in self._file_path.lower()): # 이미지 파일이 아닌 경우 바로 종료
            return ["Need to image file"]
        
        self.read_image() # 이미지 읽어오기
        # self.bln_rotate() # 이미지 회전이 필요한지 확인한 후, 회전
        self.image_preprocessing() # 이미지 전처리
        result = self._ocrReader.readtext(self._img) # OCR Text 읽기

        for bbox, text, conf in result: # bbox(해당 text의 위치), text(추출된 문자), conf(정확도)
            if conf >= self._THRESHOLD: # conf(정확도)가 THRESHOLD 이상일 때만 리스트에 s담는다.
                self.ocrResult = text # Setter로 결과값 넣어주기
                cv2.rectangle(
                    self._img, 
                    pt1=(int(bbox[0][0]), int(bbox[0][1])), 
                    pt2=(int(bbox[2][0]), int(bbox[2][1])), 
                    color=(0, 255, 0), 
                    thickness=3
                ) # image에 사각형 표시
        print(self.ocrResult)
        print("RPA S맨 : 이미지에서 텍스트 추출 작업 완료.")
        self.show_image() # 결과 보기

if __name__ == '__main__':
    myocr_ = myocr('./data/bills_sample1.jpg', 0.5)
    myocr_.ocr_process() # ocr 작업 시작
    print(myocr_.ocrResult) 
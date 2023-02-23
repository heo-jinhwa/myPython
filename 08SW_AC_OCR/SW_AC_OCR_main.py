# pyinstaller -F 파일명.py --collect-all easyocr
# Is poppler installed and in PATH 에러 발생시 -> poppler설치하여 해결 (https://github.com/oschwartz10612/poppler-windows/releases/)
# 압축해제 후 poppler_path 경로로 옮기기
from pdf2image import convert_from_path
from RPA import RPA
from myOCR import myocr
import pandas as pd

CONNECTION_PATH = "D:/Uipath/PythonData/PythonConnection.xlsx" # 해당 경로 고정

def PdfToImage(filepath): # PDF -> IMG 파일로 변환
    print("RPA S맨 : PDF파일 -> Image파일 변환중입니다.")
    print(filepath)
    if ".pdf" not in filepath: # filepath가 pdf파일이 아닌경우는 바로 종료
        return
    img_paths = [] # img로 변환 된 경로를 담을 LIST
    pages = convert_from_path(filepath, poppler_path='C:/Program Files/poppler/Library/bin') # pdf파일에서 page별로 객체를 나눠줌

    for idx, page in enumerate(pages): 
        page.save(filepath.replace(".pdf", "")+str(idx+1)+".jpg", "JPEG") # 파일명 : pdf 파일명+idx로 생성
        img_paths.append(filepath.replace(".pdf", "")+str(idx+1)+".jpg") # list에 담아줌

    print("RPA S맨 : PDF파일 -> Image파일 변환완료.")
    return img_paths # 변환된 image 경로 LIST를 반환

def write_result_toExcel(result):
    column_name = ['page', 'result']
    df = pd.DataFrame(result, columns=column_name, index=False)
    df.to_excel('/result.xlsx')

def main_process(RPAobject):
    input_files = RPAobject.get_input_files()
    if len(input_files) == 0: # input파일이 없는 경우 바로 종료
        raise Exception("input파일이 없습니다.")
    convert_images = PdfToImage(input_files[0]) # 첫번째 파일 가져오기(full 경로)) 

    result = []
    for number, image in enumerate(convert_images):
        myocr_ = myocr(image, 0.3) # image, threshold
        myocr_.ocr_process() # ocr 작업 시작
        result.append([number+1, myocr_.ocrResult]) # page number, ocr 결과
    write_result_toExcel(result)
    
if __name__ == '__main__':
    try:
        myRPA = RPA(CONNECTION_PATH) 
    except:
        raise Exception(CONNECTION_PATH+" 파일을 확인해주세요.")
    
    print("Python RPA 수행 시작")
    main_process(myRPA)
    print("Python RPA 수행 완료")
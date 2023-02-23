# pip install pillow (해당 python 환경에 설치-RPA 배포 시 RPA 로봇 python에도 설치 필요)
# pip install pytesseract (해당 python 환경에 설치-RPA 배포 시 RPA 로봇 python에도 설치 필요)
# https://pypi.org/project/pytesseract/
# https://github.com/UB-Mannheim/tesseract/wiki 설치경로 (tesseract 파일 설치)
# 성능이 그닥인거 같음
from PIL import Image
import pytesseract

def OcrPytesseract(filepath, in_lang):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' # tesseract 경로
    result = pytesseract.image_to_string(Image.open(filepath), lang=in_lang)
    return result # string으로 반환

if __name__ == '__main__':
    full_string = OcrPytesseract(r'D:\★ 업무 ★\9. RPA\00. 소스\UiPath_Python\SW_Framework\Python_Script\img_data\abc1.jpg', 'eng') # 절대경로로 해야 UiPath에서 수행 가능
    print(full_string)
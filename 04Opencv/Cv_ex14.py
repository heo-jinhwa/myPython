import cv2
import numpy as np

# 1. 경계선 검출
def empty():
    pass

def CannyEdgeDetection():
    img = cv2.imread('./data/img.jpg')
    name = 'trackbar'
    cv2.namedWindow(name)
    cv2.createTrackbar('threshold1', name, 0, 255, empty) # min_val
    cv2.createTrackbar('threshold2', name, 0, 255, empty) # max_val

    while True:
        threshold1 = cv2.getTrackbarPos('threshold1', name)
        threshold2 = cv2.getTrackbarPos('threshold2', name)
        
        canny = cv2.Canny(img, threshold1, threshold2) # 대상 이미지, min_val(하위 임계값), max_val(상위 임계값)

        cv2.imshow('gray', img)
        cv2.imshow(name, canny)

        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()

if __name__ == '__main__':
    CannyEdgeDetection()
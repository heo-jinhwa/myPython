import cv2
import numpy as np

class myMiniProject:
    def __init__(self, img_title, src_img, drawing):
        self._point_list = []
        self._img_title = img_title
        self._src_img = cv2.imread(src_img)
        self._drawing = drawing # 선 그릴지 여부
        self._THICKNESS = 3 # 선 두께
        self._COLOR = (255, 0, 255)

    def mouse_handler(self, event, x, y, flags, param):
        dest_img = self._src_img.copy() # 실시간 복사본에다가 새로 그려줌 (선 갱신)
        if event == cv2.EVENT_LBUTTONDOWN: # 마우스 왼쪽 버튼 Down
            self._drawing = True # 선을 그리기 시작
            self._point_list.append((x, y))
        
        if self._drawing:
            prev_point = None # 직선의 시작점
            for point in self._point_list:
                cv2.circle(self._src_img, point, 15, self._COLOR, cv2.FILLED)

                if prev_point:
                    cv2.line(dest_img, prev_point, point, self._COLOR, self._THICKNESS, cv2.LINE_AA)
                prev_point = point

            next_point = (x, y)
            if len(self._point_list) == 4:
                self.show_result() # 결과 출력
                next_point = self._point_list[0] # 첫 번째 클릭한 점
            cv2.line(dest_img, prev_point, next_point, self._COLOR, self._THICKNESS, cv2.LINE_AA)

        cv2.imshow(self._img_title, dest_img)

    def show(self):
        cv2.namedWindow(self._img_title)
        cv2.setMouseCallback(self._img_title, self.mouse_handler)
        cv2.imshow(self._img_title, self._src_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    def show_result(self):
        width, height = 530, 710
        
        src = np.float32(self._point_list)
        dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)
        # 좌상, 우상, 우하, 좌하 (시계 방향으로 4지점 정의)
    
        matrix = cv2.getPerspectiveTransform(src, dst) # Matrix를 얻어옴 (src영역 -> dst영역)
        result = cv2.warpPerspective(self._src_img, matrix, (width, height)) # matrix대로 변환
        cv2.imshow('result', result)

if __name__ == '__main__':
    myInstance = myMiniProject('img', './data/poker.jpg', False)
    myInstance.show()
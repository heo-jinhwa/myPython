import os
import pandas as pd
import pickle
from sklearn import model_selection
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

class Diamond:
    def __init__(self, datafile):
        self._datafile = datafile
        self._model = None
        self._modelfilename = None
        self._df = None
        self._train_data = [] # X_train, Y_train
        self._test_data = [] # X_test, Y_test

    # 데이터 파일 읽기
    def read_data(self):
        self._df = pd.read_csv(self._datafile)

    # 데이터 정제 (numerical 변환)
    def data_preprocessing(self):
        categorical_features = ['cut', 'color', 'clarity']
        le = LabelEncoder()
        for i in range(3):
            new = le.fit_transform(self._df[categorical_features[i]]) # 카테고리별 숫자(int) 값으로 변환해줌
            self._df[categorical_features[i]] = new

    # 데이터 나누기
    def data_split(self):
        array = self._df.values
        X = array[:, 0:6] # 0~5열만 추출 (관련 데이터)
        y = array[:, 6] # 6열만 추출 (결과 데이터 -> 가격)
        
        # 훈련/테스트 데이터 분할 
        X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, y, test_size=0., random_state=7)
        self._train_data.append(X_train)
        self._train_data.append(Y_train)
        self._test_data.append(X_test)
        self._test_data.append(Y_test)

    # 모델링 및 테스트
    def modeling(self, model_filename='model_50.sav'):
        self._modelfilename = model_filename
        self._model = RandomForestRegressor(n_estimators=50, max_depth=10, random_state=101)
        self._model.fit(self._train_data[0], self._train_data[1]) # X_train, Y_train
        result = self._model.score(self._test_data[0], self._test_data[1]) # X_test, Y_test
        print(result)

        # 훈련된 모델 저장
        pickle.dump(self._model, open(model_filename, 'wb'))

def pricePrediction(in_file,  modelFile): # UiPath에서 호출할 함수 (결과 저장 로직)
    # 예측 대상 데이터 읽어오기
    myData = pd.read_csv(in_file)
    categorical_features = ['cut', 'color', 'clarity']
    le = LabelEncoder()

    # 데이터 정제 (numerical 변환)
    for i in range(3):
        newValue = le.fit_transform(myData[categorical_features[i]])
        myData[categorical_features[i]] = newValue
    array = myData.values
    X = array[:, 0:6]
    
    # 훈련데이터 모델 가져오기
    loaded_model = pickle.load(open(modelFile), 'rb')
    Y_pred = loaded_model.predict(X).astype(int) # 모든 타입이 같을 때만 df.astype('타입')을 해야함 -> 하나라도 다른 type이 있으면 에러

    # 예측 결과 파일 저장
    out_file = in_file.split('.')[0]+"_pred_price.csv"
    myData['pred_price'] = pd.Series(Y_pred, index=myData.index)
    myData.to_csv(out_file)

if __name__ == '__main__':
    dm = Diamond('./data/train_data.csv')
    dm.read_data()    
    dm.data_preprocessing()
    dm.data_split()
    dm.modeling()
    

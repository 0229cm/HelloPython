# -*- coding: utf-8 -*-
"""머신러닝03-traintest.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vZ9gLyOLvM7ala8GIeQhAnhdUkoQUMU9

# 훈련과 테스트 데이터
* 머신러닝 모델을 만들기 위해서 데이터 집합이 필요
* 과적합을 방지하기 위해 데이터를 훈련/테스트 데이터로 나누고
* 교차검증 방식으로 모델을 만들어 성능을 평가함

* 훈련데이터 : 모델 추정 및 학습이 목적
* 테스트데이터: 모델 성능 평가가 목적
* 분할 비율은 7:3 또는 8:2 로 설정
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn

# train/test 데이터 분할 필요성 알아보기
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 데이터 적재
iris = load_iris()
data = iris.data # 독립변수
label = iris.target # 종속변수

dtclf = DecisionTreeClassifier()
dtclf.fit(data, label) # 주어진 독립변수와 종속변수로 학습시킴(fit)
predict = dtclf.predict(data) # 학습된 모델에 종속변수를 이용해서 예측해봄

print('모델정확도', accuracy_score(label, predict)) # 예측값과 실제값을 비교해서 정확도를 산출해 봄
# 모델을 학습할때 사용한 데이터를 모델을 평가할때도 사용함 => 정확도 1
# 비유) A문제집으로 시험공부 했는데, 시험문제가 A문제집에서 거의 다나옴 => 100점
# 이런문제를 피하려면 데이터셋을 훈련/테스트로 나눠 학습과 평가를 수행해야 함

# 데이터를 학습용/평가용 데이터로 분할 1
# 학습용/평가용 데이터 비율은 7:3으로 설정
# iris 총 데이터는 150개이므로 
# 학습용/평가용 데이터수는 105:45로 설정

train_data = iris.data[:105,]
test_data = iris.data[105:,]
print(train_data.shape,test_data.shape)

train_tar
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------get = iris.target[:105,]
test_target = iris.target[105:,]
print(train_target.shape, test_target.shape)

import pandas as pd
# 데이터 분할 상의 문제는 없는지 확인해 봄
print(pd.Series(train_target).value_counts())
print(pd.Series(test_target).value_counts())
# 데이터를 앞에서 순서대로 나눴기 때문에
# 데이터 비율이 일정하지 않음
# 즉, setosa, verginica, versicolor 의 비율이
# 같아야 하는데, train에는 setosa, verginica 위주로
# test에는 versicolor 위로로 데이터가 분할됨

# 따라서, setosa, verginica들은 잘 구분하지만
# versicolor는 잘 예측하지 못하는 경우 발생함
dtclf = DecisionTreeClassifier()
dtclf.fit(train_data, train_target)
predict = dtclf.predict(test_data)
print('정확도', accuracy_score(test_target, predict))
# 모델을 학습할때 사용한 데이터를 
# 모델을 평가할때도 사용함 => 정확도 1
# 과적합overfit 발생
# 훈련데이터가 가지고 있는 특성을 너무많이 반영해서
# 훈련데이터의 패턴을 너무 잘 인식하게 되는 문제
# 이런경우 새로운 데이터가 주어지면
# 정확하게 예측하는 일반화능력은 떨어짐

import pandas as pd
# 데이터 분할 상의 문제는 없는지 확인해 봄
print(pd.Series(train_target).value_counts())
print(pd.Series(test_target).value_counts())
# 데이터를 앞에서 순서대로 나눴기 때문에
# 데이터 비율이 일정하지 않음
# 즉, setosa, verginica, versicolor 의 비율이
# 같아야 하는데, train에는 setosa, verginica 위주로
# test에는 versicolor 위로로 데이터가 분할됨

# 따라서, setosa, verginica들은 잘 구분하지만
# versicolor는 잘 예측하지 못하는 경우 발생함

# 데이터를 학습용/평가용 데이터로 분할 2
# 독립변수의 속성들의 분포를 고려한 표본추출 필요
# => sklearn의 train_test_split 함수를 사용
# train_test_split(독립변수, 종속변수, 훈련데이터크기, 평가데이터크기, 계층추출여부(분류용), 난수시드값)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, train_size=0.7,test_size=0.3, stratify=iris.target, random_state=2007281600)

print(pd.Series(y_train).value_counts())
print(pd.Series(y_test).value_counts())

dfclf = DecisionTreeClassifier
dtclf.fit(X_train, y_train)
predict = dtclf.predict(X_test)
print('정확도', accuracy_score(y_test, predict))

# 데이터를 학습용/평가용 데이터로 분할 3
# 데이터수가 작은 경우 데이터의 일부인 평가 데이터도 작음
# => 성능 평가의 신뢰도 의심
# 데이터를 동일한 크기로 k개 나누고 이들 중 훈련/평가 데이터를 구분지어
#순환적으로 훈련 및 평가를 k번 실시함
# = > k fold 교차검증이라 함
# => sklearn의 cross_val_score 함수를 사용
# cross_val_score(분류기, 데이터, 레이블, 평가방식, 폴드수)
import numpy as np
from sklearn.model_selection import cross_val_score

dtclf = DecisionTreeClassifier()
scores = cross_val_score(dtclf, iris.data, iris.target, scoring='accuracy', cv=5)

print('교차검증 정확도', scores)
print('평균 교차검증 정확도', np.mean(scores))
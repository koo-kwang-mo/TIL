import tensorflow as tf
import numpy as np
import keras

x_train = np.array([[0], [1]])
y_train = x_train * 2 + 1

x_test = np.array([[2], [3]])
y_test = x_test * 2 + 1


#순차모델 생성
model = keras.models.Sequential()


#모델의 Layer 구성하기

#첫번째 레이어로 1입력 , 2출력이다.
model.add(tf.keras.layers.Dense(2, input_shape=(1,)))

#두번쨰 레이어는 입력 갯수를 추가해줄 필요가 없다. 1출력
model.add(tf.keras.layers.Dense(1))
#텐서플로우 2.xx버전 이상에서는 keras -> tf.keras로 바꾸면 에러해결


#학습시키기

#학습이전 예측값
pre_train_y_predict = model.predict(x_test)
print(pre_train_y_predict)

model.compile('SGD', 'mse')
hist = model.fit(x_train,y_train, epochs = 1000, batch_size = 2, verbose = 0)

y_predict = model.predict(x_test)
print(y_predict)
# 케라스 공부

## Layer의 종류들

### Dense Layer

<img src='Dense Layer.JPG'>

다층 퍼셉트론 신경망에서 사용되는 레이어이며 입력과 출력은 모두 연결 되어 있다.
 => 총 연견선의 개수는 입력 X 출력이 된다.
 각 연결선은 가중치를 가지고 있으며 이 가중치는 연결강도를 의미한다.

 from tensorflow.python.keras.layers import Dense
Dense(8,input_dim=4,activation='relu')

 - 첫 번째 인자는 출력 뉴런의 수 이며
 - input_dim 은 입력 뉴런의 수를 의미한다.
 - activation은 활성화 함수로 4가지 값이 존재한다.
   - leaner : 디폴트 값으로 입력 뉴런과 가중치로 계산된 결과 값이 그대로 출력
   - relu : rectifier 함수로 은닉층에서 주로 사용된다.
   - sigmoid : 시그모이드 함수로 이진 분류 문제에서 출력 층에 주로 쓰임
   - softmax : 다중 클래스 분류 문제의 출력 층에 주로 쓰임.


### Convolution Layer

<img src='Convolution Layer.JPG'>

Convolution Layer 신경망은 다층 퍼셉트로 신경망과 유사하나 이미지가 가지고 있는 특성을 고려하여 설게뙴
 => 영상 처리에 주로 사용됨.
 Convolution Layer의 신경망 모델의 주요 레이어로 3가지가 있다.
  - Convolution Layer
  - Max pooling Layer
  - Flatten Layer
 많은 종류가 있지만 케라스에서 자주 사용되는 Conv2D Layer를 살펴보자.

from tensorflow.python.keras.layers.convolutional import Conv2D
Conv2D(32,(5,5), padding='valid',input_shape=(28,28,1),activation='relu')

 - 첫 번째 인자 : Convolution filter의 수
 - 두 번째 인자 : Convolution filter의 사이즈
 - Padding : 경계 처리 방법
   - vaild : 유효한 영역만 출력 => 출력 이미지는 입력보다 작다.
   - same : 출력 이미지가 입력 사이즈와 동일
 - input_shape : 샘플 수를 제외한 입력 형태를 정의. 모델에서 첫 레이어 일때만 정의하면 된다. 행, 열, 채널 수로 정의된다.
   - 흑백 : 1, 컬러(RGB) : 3
 - activation : 4가지 값이 존재.
   - leaner : 디폴트 값으로 입력 뉴런과 가중치로 계산된 결과 값이 그대로 출력
   - relu : rectifier 함수로 은닉층에서 주로 사용된다.
   - sigmoid : 시그모이드 함수로 이진 분류 문제에서 출력 층에 주로 쓰임
   - softmax : 다중 클래스 분류 문제의 출력 층에 주로 쓰임.

### Max Pooling Layer

<img src='Max Pooling Layer.JPG'>

Convolution Layer의 출력 이미지에서 주요 값만 뽑아 작은 크기로 만듦.

from tensorflow.python.keras.layers.convolutional import MaxPooling2D
MaxPooling2D(pool_size=(2,2))

- pool_size : 수직, 수평 축소 비율을 지정.
  - (2,2)라면 출력 영상 크기를 입력 영상 크기의 반으로 줄인다.


### Flatten Layer

<img src='Flatten Layer.JPG'>

Convolution Layer나 Max Pooling Layer를 반복적으로 거치며 주요 특징만 추출되고 추출된 주요 특징은 전결합층에 전달되어 학습된다. 전결합층에 전달하기 위해 1차원 자료로 바꿔주는데 이 때 사용되는 Layer

from tensorflow.python.keras.layers import Flatten 
Flatten()


## 모델 형성

위에 설명된 여러 Layer들을 적절히 활용하여 모델을 만들 수 있다.
아래 예시로

Conv2D Layer -> MaxPooling2D Layer -> Conv2D Layer -> MaxPooling2D Layer -> Flatten Layer -> Dense Layer
로 이뤄진 모델을 만드는 코드를 살펴보자.


import numpy
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.layers import Flatten
from tensorflow.python.keras.layers.convolutional import Conv2D
from tensorflow.python.keras.layers.convolutional import MaxPooling2D
from tensorflow.python.keras.utils import np_utils

model = Sequential()

model.add(Conv2D(2,(3,3),padding='same',activation='relu',input_shape=(8,8,1)))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(3,(2,2),padding='same',activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(8,activation='relu'))
model.add(Dense(3,activation='softmax'))


+) 가시화하는 코드

from IPython.display import SVG
from tensorflow.python.keras.utils.vis_utils import model_to_dot

%matplotlib inline

SVG(model_to_dot(model,show_shapes=True).create(prog='dot',format='svg'))


### LSTM(Long Short - Term Memory units) Layer

컨볼루션 신경망 뿐만 아니라 순환 신경망 모델이라는 것도 존재하는데 이는 순차적인 자료에서 규칙적인 패턴을 인식하거나 그 의미를 추론할 수 있다. 순차적이라는 특성 때문에 간단한 레이어로도 다양한 형태의 모델을 구성할 수 있다.

LSTM(3, input_dim=1, input_length=5)
 - 첫 번쨰 인자 : 메모리 셀의 개수
 - input_dim : 입력 속성 수
 - input_length : 시퀸스 데이터의 입력 길이
 - return_sequences : 시퀸시 출력 여부

=> Dense Layer와 비슷한데 첫 번째 인자인 메모리 셀의 개수는 기억용량 정도와 출력 형태를 결정 짓는다. Dense 레이어에서의 출력 뉴런 수와 비슷하다고 보면 된다.


출처 : https://ssongnote.tistory.com/m/13
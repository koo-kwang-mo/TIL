# 1. Model 생성하기(순차 모델)
   1. 일반적으로 모델을 생성하고 type을 찍어보면 keras 자체 엔진에서 제공하는 sequential class를 통해 생성됨을 알 수 있다.
   2. add 함수를 사용해서 model에 node를 추가할 수 있다.
      - 이미 model 내부에 있는 node들과 현재 추가하는 node를 연결할 수 있다.  
   3. Dense 함수는 input과 output을 모두 연결해주는 NN Layer이다. keras는 Dense를 class로 구현하였으며 Dense로 만들어준 node는 weight와 bias 변수를 각각 갖게 된다.
   
    ## model = keras.models.Sequential() #모델 생성
    ## model.add(keras.layers.Dense(1, input_shape(1,)))
       - input, output이 1개인 노드를 만들었다.
       - input_shape(1,) 대신 input_dim = 1로 해도 됨


# 2. Model 학습시키기
   1. 학습 전, compile 함수를 사용하여 여러 설정을 해 줄 수 있다.
      - optimizer : 학습과정에서 최적화 방식을 설정해준다.
        - adam 이나 sgd처럼 문자열로 선언할 수 있다.
      - loss : loss 인자는 loss function을 설정하는 인자이며 regression의 경우 mean_squared_error(평균 제곱 오차)를 사용할 수 있고
        - multi class classification의 경우 범주형 교차 엔트로피를 사용할 수 있다.
      - metircs : 학습을 모니터링하기 위한 지표
   2. 모델을 학습 시키는 함수는 fit이다. 총 4가지의 인자가 존재한다.
      - training data set
      - x_train, y_train
      - epoch : 학습 횟수
      - batch_size : 기본값은 32, 한 번에 학습하는 사이즈
    +) vaildation_data는 검증 데이터를 사용하는 경우,
    vaildation_split은 학습 데이터의 일부를 검증 데이터로 사용. valiation_split은 validation_data 대신에 사용할 수 있다.
    verbose는 학습 중 출력할 문구이며 1은 훈련 진행도를 의미하는 막대, 2는 미니 배치마다 loss 정보를 출력한다.

    ## model.fit(x_train, y_train, epochs = 1000, batch_size = 2, verbose = 0)


# 3. Model 평가하기.
   1. evaluate : 정확도를 평가, 3가지 인자가 존재한다
      - x_test
      - y_test
      - batch_size

    ## model.evaluate(x_test, y_test, batch_size = 2)


# 4. Model 예측하기
 1. predict : 어떤 입력에 대한 모델의 출력값을 확인해주는 함수, 2가지 인자를 받는다.
      - 예측하고자 하는 데이터
      - batch_size
   
    ## y_predict = model.predict(x_test, batch_size = 2)



출처 : https://hyuna-tech.tistory.com/entry/Keras-Sequential-Model-%EC%88%9C%EC%B0%A8%EB%AA%A8%EB%8D%B8-%EC%82%AC%EC%9A%A9-%EC%98%88%EC%A0%9C-%EB%8B%A8%EC%9D%BC-layer
      

      
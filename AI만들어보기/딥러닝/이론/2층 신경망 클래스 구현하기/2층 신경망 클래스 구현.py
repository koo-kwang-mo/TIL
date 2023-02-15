import sys, os
sys.path.append(os.pardir)
from common.functions import *
from common.gradient import numerical_gradiant#기울기 구하는 패키지

class TwoLayerNet:
    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
    #초기화, 순서대로 입력층 뉴런, 은닉층의 뉴런, 출력층의 뉴런 수 이다.
        self.params = {}
        self.params['W1'] = weight_init_std * np.ramdom.randn(input_size, hidden_size)#1층?
        self.params['b1'] = np.zeros(hidden_size)
        self.params['W2'] = weight_init_std * np.ramdom.randn(hidden_size, output_size)#2층?
        self.params['b1'] = np.zeros(output_size)

#params 신경망의 매개변수를 보관하는 딕셔너리 변수


    def predict(self, x):   #예측 함수
        W1, W2 = self.params['W1'], self.params['W2']#가중치와
        b1, b2 = self.params['b1'], self.params['b2']#편향을 가져온다.

        a1 = np.dot(x, W1) + b1# y = ax + b 형태로 연산한 후
        z1 = sigmoid(a1)#활성화 함수 적용
        a2 = np.dot(z1, W2) + b2#적용된 내용을 다시 연산한 후
        y = softmax(a2)#활성화 함수 적용 후

        return y#출력한다.

    #x : 입력 데이터, y : 정답 데이터

    def loss(self, x, y):#손실함수 연산
        y = self.predict(x)

        return cross_entropy_error(y, t)#실제 결과값과 예측치(y) 의 차이를 반환, CEE에 대한 내용은 리드미에서 정리
    
    def accuracy(self, x, y):
        y = self.predict(x)
        y = np.argmax(y, axis = 1)
        t = np.argmax(t, axis = 1)
        # argmax 함수 : 행렬에서 가장 값이 높은 인덱스 번호 반환. axis = 1은 가로축, axis = 0또는 안 적으면 세로축.
        
        accuracy = np.sum(y == t) / float(x.shape[0])
        return accuracy
    

    def numerical_gradient(self, x, y):
        loss_W = lambda W: self.loss(x, t)

        grads = {}
        grads['W1'] = numerical_gradiant(loss_W, self.params['W1'])
        grads['b1'] = numerical_gradiant(loss_W, self.params['b1'])
        grads['W2'] = numerical_gradiant(loss_W, self.params['W2'])
        grads['b2'] = numerical_gradiant(loss_W, self.params['b2'])

#grads 기울기를 보관하는 딕셔너리 변수


        return grads
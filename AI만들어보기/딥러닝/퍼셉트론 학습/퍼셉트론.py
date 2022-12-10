import numpy as np

X = np.array([[0,0], [1,0], [0,1], [1,1]])
Y = np.array([-1,1,1,1])
#그 다음에는 퍼셉트론의 weight와 bias를 하나의 어레이로 표현했습니다. weight과 bias는 1로 초기화 되었습니다.

w=np.array([1. , 1. , 1.])  # [bias, w1, w2]
#퍼셉트론의 전방 계산을 하는 forward 함수, 부류를 예측하는 predict 함수 입니다.

def forward(x):
  return np.dot(x, w[1:]) + w[0]

def predict(X):
  return np.where(forward(X) > 0, 1, -1)
#함수를 업데이트 하고 학습 전후를 비교합니다.

print("predict (before traning)", w)

for epoch in range(50):
  for x_val, y_val in zip(X, Y):
    update = 0.01 * (y_val - predict(x_val))
    w[1:] += update * x_val#시그마 wi*xi를 표현
    w[0] += update

print("predict (after traning)", w)

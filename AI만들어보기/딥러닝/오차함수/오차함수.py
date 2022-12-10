#임의의 기울기와 y절편 정의
line_a_b = [2, 1]#함수,예측?
#이 함수가 데이터를 가장 잘나타내는 함수인가?

#아니면 하나의 예측으로써 여러개의 함수들 중 오차함수가 낮은 것을 택하는가?
#+) 이게 맞는거 같음


#데이터, 실제 값
data = [[1,4], [3,9], [4, 10], [7,13]]
x = [i[0] for i in data]
y = [i[1] for i in data]

#예측
predict_result = []

def predict(x):
    return line_a_b[0]*x + line_a_b[1]#기울기가 a, 절편이 b인 함수에 대입

for i in range(len(x)):
    predict_result.append(predict(x[i]))
    print("공부시간 = %.f, 실제점수 = %.f, 예측점수 = %.f"%(x[i], y[i], predict[x[i]]))


#MSE  구하기

def mse_val(predict_result, y):
    return mse(np.array(predict_result, np.array(y)))

def mse(y_hat, y):#README에 있는 수식표현, 오차들 제곱의 평균
    return((y_hat-y)**2).mean()


# 출처 : https://likethefirst.tistory.com/entry/Python-%EC%84%A0%ED%98%95%ED%9A%8C%EA%B7%80-2-a%EC%99%80-b%EC%97%90-%EB%94%B0%EB%A5%B8-%ED%8F%89%EA%B7%A0-%EC%98%A4%EC%B0%A8-%EC%A0%9C%EA%B3%B1MSE-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%ED%95%98%EA%B8%B0-%EC%84%A0%ED%98%95%ED%9A%8C%EA%B7%80-%EC%8B%A4%EC%8A%B5?category=935632
def numerical_gradient(f,x):#기울기 구하는 함수
    h = 1e-4
    grad = np.zeros_like(x)

    for idx in range(x.size):
        tmp_val = x[idx]
        
        #f(x+h) 계산
        x[idx] = tmp_val + h
        fxh1 = f(x)

        #f(x-h) 계산
        x[idx] = tmp_val - h
        fxh2 =f(x)

        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val
    
    return grad





def gradient_descent(f, init_x, lr = 0.01, step_num =100): #초기 학습률 0.01, 배치사이즈 100 설정
    x = init_x

    for i in range(step_num):
        grad = numerical_gradient(f,x)#위의 기울기 구하는 함수
        x -= lr * grad
    
    return x

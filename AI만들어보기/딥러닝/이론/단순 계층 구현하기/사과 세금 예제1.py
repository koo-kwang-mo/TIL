class MulLayer:
    def __init__(self):
        self.x = None
        self.y = None
    
    def forword(self, x, y):
        self.x = x
        self.y = y
        out = x * y

        return out
    
    def backword(self, dout):
        dx = dout * self.y #x와 y를 바꾼다
        dy = dout * self.x

        return dx, dy
        
apple = 100
apple_num = 2
tax = 1.1

#계층들
mul_apple_layer = MulLayer()
mul_tax_layer = MulLayer()

#순전파
apple_price = mul_apple_layer.forword(apple, apple_num)
price = mul_tax_layer.forword(apple_price, tax)

#역전파
dprice = 1
dapple_price, dtax = mul_tax_layer.backword(dprice)
dapple, dapple_num = mul_apple_layer.backword(dapple_price)

print(dapple, dapple_num, dtax)# 2.2 110 200

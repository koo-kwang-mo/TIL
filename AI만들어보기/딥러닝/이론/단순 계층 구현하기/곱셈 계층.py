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
        
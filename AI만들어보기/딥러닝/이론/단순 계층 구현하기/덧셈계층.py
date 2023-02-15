class AddLayer:
    def __init__(self):
        pass
    def forword(self, x, y):
        out = x + y
        return out
    def backword(self, dout):
        dx = dout * 1
        dy = dout * 1
        return dx, dy

class A:
    def __init__(self):
        self.n = "A"

class B(A):
    pass

class C(A):
    def __init__(self):
        self.n = "C"

class D(B,C):
    pass


# 新式类从左到右宽度优先
d = D()
print(d.n)
print(D.__mro__)

class test:
    b = 4
    def __init__(self):
        self.a = 3
        print(__class__)
        ff = __class__
        print(ff.b)
mm = test()
x = type(mm)
print(x.b)
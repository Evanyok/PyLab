class Singleton3(object):
    __shared_state = {"1","2"}
    def __init__(self):
        self.x = 1
        self.__dir__ = self.__shared_state
        pass

b = Singleton3()
b1 = Singleton3()
print(b)
print(b.__dir__)
print(b1)
print(b1.__dir__)
b.x = 4
print(b)
print(b.__dir__)
print(b1)
print(b1.__dir__)
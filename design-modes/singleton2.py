class Singleton2(object):
    __instance = None
    def __init__(self):
        if not Singleton2.__instance:
            print("__init__ method is called...")
        else:
            print("Instance is already created: ", self.getInstance())
        
    @classmethod    
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton2()
        return cls.__instance

s = Singleton2()
s.getInstance()

s1 = Singleton2()
s1.getInstance()
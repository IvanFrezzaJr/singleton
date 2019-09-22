#
# Singleton instantiating class
#
class clsSingleton1(object):
    _instance = None
    def __new__(self):
        if not self._instance:
            self._instance = super(clsSingleton1, self).__new__(self)
        return self._instance
        

#
# Singleton instantiating class and using getInstance class method
#
class clsSingleton2(object):
    _instance = None
    def __new__(self):
        return self.getInstance()
    
    @classmethod
    def getInstance(cls):
        if not cls._instance:
            cls._instance = super(clsSingleton2, cls).__new__(cls)
        return cls._instance


#
# Singleton using decorator
#
def singleton(myClass):
    __instances = {}
    def getInstance(*args, **kargs):
        if myClass not in __instances:
            __instances[myClass] = myClass(*args, **kargs)        
        return __instances[myClass]
    return getInstance

@singleton
class clsSingleton3(object):
    pass


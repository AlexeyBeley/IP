import pdb


class gsd(property):
    a = 0
    def __init__(self):
        self.b = 1
    
    def c(self):
        return 2
    
    def __get__(self, instance, owner):
        pdb.set_trace()

#__get__, __set__ and __delete__ 
self = gsd()

def a():
    pass
a.a = 1
print(a.a)
print("*")
pdb.set_trace()
print(gsd.a)
print(self.b)
print(self.a)
print(self.c())
print(self.c)


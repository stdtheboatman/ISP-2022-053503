import math
from factory import Creator

ser = Creator.create_serializer("json")

y = 4
def foo(x):
    z = 3
    return math.sin(x + y + z)

def test_func():
    s = ser.dumps(foo, globals())
    bar = ser.loads(s)
    
    assert(foo(3) == bar(3))
    

class Cat:
    def __init__(self, name: str):
        self.name = name
        
    def pet(self) -> str:
        return "u pet a " + self.name
    
def test_class():
    cat = Cat("Cat")
    s = ser.dumps(Cat, globals())
    Cat1 = ser.loads(s)
    
    cat1 = Cat1("Cat")
    
    #print(cat.pet())
    #print(cat1.pet())
    assert(cat.pet() == cat1.pet())
    
    

if __name__ == "__main__":
    test_func()
    test_class()
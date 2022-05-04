import math
from factory import Creator

ser = Creator.create_serializer("json")

y = 4
def foo(x):
    z = 3
    return math.sin(x + y + z)

def test_func():
    s = ser.dumps(foo)
    bar = ser.loads(s)
    
    assert(foo(3) == bar(3))
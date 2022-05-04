import json
from baisc_serializator import Serializator
from mypickle import MyPickle

class JsonSerializator(Serializator):
    def dumps(self, obj: object) -> str:
        ser_obj = MyPickle.serialize(obj)
        return json.dumps(ser_obj)
    
    def dump(self, obj: object, filepath: str) -> None:
        ser_obj = MyPickle.serialize(obj)
        
        with open(filepath, "w") as file:
            json.dump(ser_obj, file)    
            
    def loads(self, s: str) -> object:
        ser_obj = json.loads(s)
        return MyPickle.deserialize(ser_obj)
    
    def load(self, filepath: str) -> object:
        ser_obj = object()
        with open(filepath, "r") as file:
            ser_obj = json.load(file)
            
        return MyPickle.deserialize(ser_obj)
    
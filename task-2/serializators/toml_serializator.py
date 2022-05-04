import toml
from baisc_serializator import Serializator
from mypickle import MyPickle

class TomlSerializator(Serializator):
    def dumps(self, obj: object) -> str:
        ser_obj = MyPickle.serialize(obj)
        
        return toml.dumps(ser_obj)
    
    
    def dump(self, obj: object, filepath: str) -> None:
        ser_obj = MyPickle.serialize(obj)
        
        with open(filepath, "w") as file:
            toml.dump(ser_obj, file)    
            
    def loads(self, s: str) -> object:
        ser_obj = toml.loads(s)    
        
        return MyPickle.deserialize(ser_obj)
    
    def load(self, filepath: str) -> object:
        ser_obj = object()
        with open(filepath, "r") as file:
            ser_obj = toml.load(file)
            
        return MyPickle.deserialize(ser_obj)
    
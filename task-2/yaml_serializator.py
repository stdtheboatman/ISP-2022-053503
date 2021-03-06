import yaml
from baisc_serializator import Serializator
from mypickle import MyPickle

class YamlSerializator(Serializator):
    def dumps(self, obj: object, _globals) -> str:
        ser_obj = MyPickle.serialize(obj, _globals)
        return str(yaml.dump(ser_obj))    
    
    
    def dump(self, obj: object, filepath: str, _globals) -> None:
        ser_obj = MyPickle.serialize(obj, _globals)
        
        with open(filepath, "w") as file:
            yaml.dump(ser_obj, file)    
            
    def loads(self, s: str) -> object:
        ser_obj = yaml.load(s, Loader=yaml.FullLoader)        
        
        return MyPickle.deserialize(ser_obj)
    
    def load(self, filepath: str) -> object:
        ser_obj = object()
        with open(filepath, "r") as file:
            ser_obj = yaml.load(file, Loader=yaml.FullLoader)
            
        return MyPickle.deserialize(ser_obj)
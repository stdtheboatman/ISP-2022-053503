from abc import ABC, abstractmethod

class Serializator(ABC):
    @abstractmethod
    def dumps(obj: object, _globals) -> str:
        pass
    
    @abstractmethod
    def dump(obj: object, filepath: str, _globals) -> None:
        pass
    
    @abstractmethod
    def loads(s: str) -> object:
        pass    
    
    @abstractmethod
    def load(filepath: str) -> object:
        pass
    
        
        
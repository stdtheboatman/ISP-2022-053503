from abc import ABC, abstractmethod

class Serializator(ABC):
    @abstractmethod
    def dumps(obj: object) -> str:
        pass
    
    @abstractmethod
    def dump(obj: object, filepath: str) -> None:
        pass
    
    @abstractmethod
    def loads(s: str) -> object:
        pass    
    
    @abstractmethod
    def load(filepath: str) -> object:
        pass
    
        
        
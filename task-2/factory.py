from baisc_serializator import Serializator

from json_serializator import JsonSerializator
from yaml_serializator import YamlSerializator
from toml_serializator import TomlSerializator 

class Creator:
    @staticmethod
    def create_serializer(name: str) -> Serializator:
        if name == "json":
            return JsonSerializator()
        
        if name == "yaml":
            return YamlSerializator
        
        if name == "toml":
            return YamlSerializator
            
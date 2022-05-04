from serializators.baisc_serializator import Serializator

from serializators.json_serializator import JsonSerializator
from serializators.yaml_serializator import YamlSerializator
from serializators.toml_serializator import TomlSerializator 

class Creator:
    @staticmethod
    def create_serializer(name: str) -> Serializator:
        if name == "json":
            return JsonSerializator()
        
        if name == "yaml":
            return YamlSerializator
        
        if name == "toml":
            return YamlSerializator
            
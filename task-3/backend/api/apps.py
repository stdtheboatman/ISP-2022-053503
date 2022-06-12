from django.apps import AppConfig
from .logic import DataHandlerSingleton

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    
    def ready(self) -> None:
        DataHandlerSingleton.getInstance()
        return super().ready()

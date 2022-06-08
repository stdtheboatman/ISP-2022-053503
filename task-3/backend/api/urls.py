from django.urls import path
from .views import setUserData

urlpatterns = [
    path('setUserData/', setUserData, name='set user data')
]
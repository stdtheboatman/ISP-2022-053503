from django.urls import path
from .views import setUserData, get

urlpatterns = [
    path('setUserData/', setUserData, name='set user data'),
    path('getCurrencyDistribution/', get, name="test_")
]
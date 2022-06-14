from operator import mod
#from django.db import models
from djongo import models
from django.contrib.auth.models import User

# Create your models here.

class UserData(models.Model):
    #id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    _id = models.ObjectIdField()
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    apiKey = models.CharField(max_length=32)
    secretKey = models.CharField(max_length=32)
    
    data = models.TextField()

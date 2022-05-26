from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserData(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True
    )

    apiKey = models.CharField(max_length=128, null=True)
    signature = models.CharField(max_length=128, null=True)
    
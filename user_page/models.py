from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(max_length=12)
    birthday = models.DateField(null=True, blank=True)
    gender = models.BooleanField(null=True, blank=True)
    photo = models.ImageField(upload_to='user_photos/', null=True, blank=True)

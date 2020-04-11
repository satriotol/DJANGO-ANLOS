from django.db import models
from django.contrib.auth.models import User

class UserPerusahaanInfo(models.Model):
    user = models.OneToOneField(User,related_name="UserPerusahaanInfo",on_delete=models.CASCADE)
    
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    
    def __str__(self):
        return self.user.username
from django.db import models
from django.contrib.auth.models import User

class UserPerusahaanInfo(models.Model):
    user = models.OneToOneField(User,related_name="UserPerusahaanInfo",on_delete=models.CASCADE)
    nama_lengkap = models.CharField(max_length=256,default='')
    email = models.EmailField(max_length=256,default='')
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    nama_perusahaan = models.CharField(max_length=256,default='')
    alamat = models.TextField(default='')    
    def __str__(self):
        return self.user.username
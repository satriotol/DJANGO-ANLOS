from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserKaryawanInfo(models.Model):
    nama_perusahaan = models.OneToOneField(User,related_name="UserKaryawanInfo",on_delete=models.CASCADE)
    nama_lengkap = models.CharField(max_length=256,default='')
    email = models.EmailField(max_length=256,default='')
    alamat = models.TextField(default='')    
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
        return self.user.username

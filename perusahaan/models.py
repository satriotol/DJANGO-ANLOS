from django.db import models
from django.contrib.auth.models import User

class UserPerusahaanInfo(models.Model):
    user = models.OneToOneField(User,related_name="UserPerusahaanInfo",on_delete=models.CASCADE)
    nama_lengkap = models.CharField(max_length=256,default='')
    email = models.EmailField(max_length=256,default='')
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    nama_perusahaan = models.CharField(max_length=256,default='')
    lokasi = models.TextField(max_length=256,default='')
    alamat = models.TextField(default='')    
    def __str__(self):
        return self.nama_perusahaan

class UserKaryawanInfo(models.Model):
    # nama_perusahaan = models.OneToOneField(UserPerusahaanInfo,related_name="UserKaryawanInfo",on_delete=models.CASCADE)
    nama_perusahaan = models.OneToOneField(
        UserPerusahaanInfo,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    nama_lengkap = models.CharField(max_length=256,default='')
    email = models.EmailField(max_length=256,default='')
    alamat = models.TextField(default='')    
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
        return "%s the restaurant" % self.nama_perusahaan
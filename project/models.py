from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class UserProfileInfo(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    
    def __str__(self):
        return self.user.username

class DataMahasiswa(models.Model):
    IK1A = 'IK1A'
    IK1B = 'IK1B'
    IK2A = 'IK2A'
    IK2B = 'IK2B'
    IK3A = 'IK3A'
    IK3B = 'IK3B'

    KELAS_CHOICES = [
    (IK1A,'IK1A'),
    (IK1B,'IK1B'),
    (IK2A,'IK2A'),
    (IK2B,'IK2B'),
    (IK3A,'IK3A'),
    (IK3B,'IK3B'),
    ]
    
    name = models.CharField(max_length=256)
    kelas = models.CharField(max_length=4,choices=KELAS_CHOICES,default=IK1A,)
    profile_pic = models.ImageField(upload_to='foto_mahasiswa',blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("index", kwargs={"pk": self.pk})

class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("basic_app:detail", kwargs={"pk": self.pk})
    
class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,related_name='student',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
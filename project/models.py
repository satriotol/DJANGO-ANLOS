from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from project.choice import KELAS_CHOICES


# Create your models here.
class UserProfileInfo(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    
    def __str__(self):
        return self.user.username

class DataMahasiswa(models.Model):
    name = models.CharField(max_length=256)
    kelas = models.IntegerField(choices=KELAS_CHOICES,default=1)
    profile_pic = models.ImageField(upload_to='foto_mahasiswa',blank=True)

    def __str__(self):
        return self.name
    

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
    
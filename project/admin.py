from django.contrib import admin
from project.models import School,Student,UserProfileInfo,DataMahasiswa

# Register your models here.
admin.site.register(School)
admin.site.register(DataMahasiswa)
admin.site.register(Student)
admin.site.register(UserProfileInfo)



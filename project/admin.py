from django.contrib import admin
from project.models import School,Student,UserProfileInfo,DataMahasiswa,UserProfileInfo
from perusahaan.models import UserPerusahaanInfo,UserKaryawanInfo


# Register your models here.
admin.site.register(School)
admin.site.register(DataMahasiswa)
admin.site.register(Student)
admin.site.register(UserProfileInfo)
admin.site.register(UserPerusahaanInfo)
admin.site.register(UserKaryawanInfo)



from django import forms
from django.contrib.auth.models import User
from perusahaan.models import UserPerusahaanInfo,UserKaryawanInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserPerusahaanInfo(forms.ModelForm):
    class Meta():
        model = UserPerusahaanInfo
        fields = ('nama_lengkap','email','nama_perusahaan','alamat','lokasi','profile_pic',)

class UserKaryawanInfo(forms.ModelForm):
    
    class Meta:
        model = UserKaryawanInfo
        fields = ("nama_lengkap","email","alamat","profile_pic",)
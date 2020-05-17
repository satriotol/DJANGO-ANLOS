from django.conf.urls import url
from perusahaan import views

app_name = 'perusahaan'

urlpatterns = [
    url('register/', views.register ,name='register'),
    url('userlogin/', views.user_login,name='user_login'),
    url('buat/', views.buat , name="buat"),
]

from django.conf.urls import url
from login import views

app_name = 'login'

urlpatterns = [
    url('register/', views.register ,name='register'),
    url('userlogin/', views.user_login,name='user_login'),
]

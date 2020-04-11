"""anlos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from project import views as main_views
from project.views import DataMahasiswalDetailView
from login import views as login_views
from perusahaan import views as perusahaan_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',main_views.IndexView.as_view(),name='index'),
    path('<int:pk>/',main_views.DataMahasiswalDetailView.as_view(),name='detail'),
    path('<int:pk>/update/',main_views.DataMahasiswaUpdateView.as_view(),name='update'),
    path('buat/',main_views.DataMahasiswaCreateView.as_view(),name='create'),
    path('delete/<int:pk>/',main_views.DataMahasiswaDeleteView.as_view(),name="delete"),
    path('admin/', admin.site.urls),
    # path('user/', include('login.urls')),
    # path('logout/',login_views.user_logout,name='logout'),
    # path('special/',login_views.special,name='special'),
    path('user/', include('perusahaan.urls')),
    path('logout/',perusahaan_views.user_logout,name='logout'),
    path('special/',perusahaan_views.special,name='special'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.shortcuts import render
from perusahaan.forms import UserForm,UserPerusahaanInfo

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from perusahaan import models
from django.views.generic import (View,TemplateView,ListView,DetailView,
                                CreateView,UpdateView,
                                DeleteView)

# Create your views here.

def special (request):
    return HttpResponse("You are logged in")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserPerusahaanInfo(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserPerusahaanInfo()

    return render(request,'login/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

def user_login(request):
    context_object_name = 'data_login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account Not Active")
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and Password {}".format(username,password))
            return HttpResponse("invalid login details supplied")
    else:
        return render(request,'login/login.html',{'name' : request.user.username })
 
class PerusahaanListView(ListView):
    context_object_name = 'profilperusahaan'
    model = models.UserPerusahaanInfo
    template_name = 'perusahaan/userperusahaaninfo_list.html'
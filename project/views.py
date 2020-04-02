from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View,TemplateView,ListView,DetailView,
                                CreateView,UpdateView,
                                DeleteView)
from project import models

class IndexView(ListView):
    paginate_by = 2
    context_object_name = 'data'
    model = models.DataMahasiswa
    template_name = 'index.html'
class DataMahasiswalDetailView(DetailView):
    context_object_name = 'datamahasiswa_detail'
    model = models.DataMahasiswa
    template_name = 'detail_mahasiswa.html'

class DataMahasiswaCreateView(CreateView):
    fields = ('name','kelas','profile_pic')
    model = models.DataMahasiswa
    template_name = 'datamahasiswa_form.html'
    success_url = reverse_lazy('index')


class DataMahasiswaDeleteView(DeleteView):
    context_object_name = 'data'
    model = models.DataMahasiswa
    template_name = 'datamahasiswa_confirm_delete.html'
    success_url = reverse_lazy('index')

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")


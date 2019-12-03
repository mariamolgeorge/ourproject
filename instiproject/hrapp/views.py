from django.shortcuts import render
from django.shortcuts import render
from django.urls import reverse_lazy

from adminapp.models import User,Course,Batch,Role,TimeTable,Placement,ClassRoom,Hr,Trainer
from django.views.generic import TemplateView, ListView, CreateView
from django.views import generic
from adminapp.models import Course
# Create your views here.

class hrget_home(TemplateView):

    template_name = 'adminapp/hrbase.html'

class UserCreate(CreateView):
    model=User
    fields='__all__'
    template_name = 'adminapp/studentregister.html'
    success_url=reverse_lazy('studentregister')

# class studentList(ListView):
#     model = User
 #template_name = 'adminapp/studentregister.html'

class TrainerCreate(CreateView):
    model=Trainer
    fields='__all__'
    template_name = 'adminapp/trainerregister.html'
    success_url=reverse_lazy('trainerregister')





# Create your views here.

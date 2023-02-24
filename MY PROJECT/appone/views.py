from django.shortcuts import render,redirect
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from appone.models import student
from django.urls import reverse_lazy
from appone.forms import STUDENTFORM


# Create your views here.
class STUDENTListView(ListView):
    model=student


class STUDENTCreateView(CreateView):
    model = student
    success_url = reverse_lazy('tabe')
    fields = '__all__'


class STUDENTUpdateView(UpdateView):
    model = student
    success_url = reverse_lazy('tabe')
    fields = '__all__'

class STUDENTDeleteView(DeleteView):
     model = student
     success_url = reverse_lazy('tabe')
     fields = '__all__'

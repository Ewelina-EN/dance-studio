from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.urls import reverse_lazy

class HomeView(TemplateView):
    template_name = 'dance_studio.html'  
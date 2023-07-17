from django.shortcuts import render
from django.views import generic as views


# Create your views here.

class HomeDetailView(views.TemplateView):

    template_name = 'base.html'

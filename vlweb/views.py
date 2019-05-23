from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

class HomeView(TemplateView):
    def get_template_names(self):
        return 'home.html'
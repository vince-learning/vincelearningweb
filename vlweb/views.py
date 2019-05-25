from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from utils import ActiveTabMixin

# Create your views here.


class HomeView(ActiveTabMixin, TemplateView):
    template_name = "home.html"
    active_tab = 'home'



class CoursView(ActiveTabMixin, TemplateView):
    template_name = "cours.html"
    active_tab = 'cours'


class ProjetsView(ActiveTabMixin, TemplateView):
    template_name = "projets.html"
    active_tab = 'projets'

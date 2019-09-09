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

class NotebooksView(ActiveTabMixin, TemplateView):
    template_name = "notebook.html"
    active_tab = 'notebooks'

# courses
class Cours1View(ActiveTabMixin, TemplateView):
    template_name = "cours/cours1.html"
    active_tab = 'cours'

class Cours2View(ActiveTabMixin, TemplateView):
    template_name = "cours/cours2.html"
    active_tab = 'cours'

class Cours3View(ActiveTabMixin, TemplateView):
    template_name = "cours/cours3.html"
    active_tab = 'cours'

class Cours4View(ActiveTabMixin, TemplateView):
    template_name = "cours/cours4.html"
    active_tab = 'cours'

class Cours5View(ActiveTabMixin, TemplateView):
    template_name = "cours/cours5.html"
    active_tab = 'cours'


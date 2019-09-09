"""vincelearningweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.conf.urls import url, include
from django.views.generic import TemplateView
from utils import ActiveTabMixin

from vlweb import views

# basic urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('cours', views.CoursView.as_view(), name='cours'),
    path('projets', views.ProjetsView.as_view(), name='projets'),
    path('notebooks', views.NotebooksView.as_view(), name='notebooks')
]

# courses urls
urlpatterns += [
    path('cours/cours1', views.Cours1View.as_view(), name='cours1'),
    path('cours/cours2', views.Cours2View.as_view(), name='cours2'),
    path('cours/cours3', views.Cours3View.as_view(), name='cours3'),
    path('cours/cours4', views.Cours4View.as_view(), name='cours4'),
    path('cours/cours5', views.Cours5View.as_view(), name='cours5'),
]

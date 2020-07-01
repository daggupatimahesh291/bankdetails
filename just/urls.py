from django.urls import path

from . import views

urlpatterns = [path('index.html', views.index, name='index'),
path('index.html', views.index, name='index'),
path('index.html', views.ifsc, name='ifsc'),
path('', views.check, name='check'),
path('branches.html', views.branch, name='branch'),
path('branches.html', views.branche, name='branche'),




]
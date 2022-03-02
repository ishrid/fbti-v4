from django import views
from django.urls import path 
from . import views

urlpatterns = [
    
    path('', views.homeViews, name='home'),
    path('albi-doro/', views.albiDoroViews, name='albiDoro') 
]

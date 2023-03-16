from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home_page, name = 'balabala1'), #home_page这种名字可以改，记得和views里对应就行了
    path('aboutme/', views.about_me, name="about_me"),
]
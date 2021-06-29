from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('profile/',views.profile,name='profile'), # p2c-21-105
    path('register/',views.register,name='register'), #p2c-21-105

]
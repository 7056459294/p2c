from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login./', views.login, name='login'),
    path('forgot_password/', views.forgot_password, name='forgot_password')

]
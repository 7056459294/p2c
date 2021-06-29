
from django.urls import path
from django.urls.conf import include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('accounts/', views.accounts, name="accounts"),
    path('courses', views.courses, name='courses')
    
]
from django.conf.urls import url , include
from django.urls import path
from . import views
from django.views.generic import ListView , DetailView
from cinema_theater.models import *


urlpatterns = [
    path('auth/login', views.auth_login, name='login'),
    path('auth/logout', views.auth_logout, name='logout'),
    path('admin/', views.admin, name='admin'),
    path('reg/', views.reg, name='registration'),
    path('', ListView.as_view(queryset=Film.objects.all().order_by('rental_start_date')[:6], template_name='cinema_theater/cinema.html')),
]

from django.urls import path
from . import views
from django.views.generic import ListView, DetailView
from cinema_theater.models import *

urlpatterns = [
    path('admin/', views.admin, name='admin'),
    # path('ticket/', views.ticket, name='ticket'),
    path('ticket/<id>', views.ticket, name='ticket'),
    path('seance/<id_room>/<id_seance>', views.seance, name='seance'),
    path('pay/<row>/<seat>/<id_room>/<id_seance>/<id_user>', views.pay, name='pay'),
    path('bin/<id_user>', views.bin, name='bin'),
    path('delite/<id_seance>/<id_seats>/<id_user>', views.delite, name='delite'),

]

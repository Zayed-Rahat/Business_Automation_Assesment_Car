from django.urls import path
from .views import *

urlpatterns = [
    path('add-car/', add_car, name='add_car'),
    path('', car_list, name='car_list'),
]

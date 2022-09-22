from django.urls import path
from .views import index, WareHouse
from . import views

app_name = 'VPHI'

urlpatterns = [
    path('', index, name='index'),
    path('Stock/',WareHouse, name='WareHouse')
]
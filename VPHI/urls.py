from django.urls import path
from .views import index, sub01, sub02, sub03, sub04, sub05

from . import views

app_name = 'VPHI'

urlpatterns = [
    path('', index.main, name='index'),

    path('sub01/sub01_01', sub01.sub01_01, name='SUB01_01'),
    path('sub01/sub01_02', sub01.sub01_02, name='SUB01_02'),
    path('sub01/sub01_03', sub01.sub01_03, name='SUB01_03'),
    path('sub01/sub01_04', sub01.sub01_04, name='SUB01_04'),
    path('sub01/sub01_05', sub01.sub01_05, name='SUB01_05'),
    path('sub01/sub01_06', sub01.sub01_06, name='SUB01_06'),
    path('sub01/sub01_07', sub01.sub01_07, name='SUB01_07'),

    path('sub02/sub02_01', sub02.sub02_01, name='SUB02_01'),
    path('sub02/sub02_02', sub02.sub02_02, name='SUB02_02'),
    path('sub02/sub02_03', sub02.sub02_03, name='SUB02_03'),
    path('sub02/sub02_04', sub02.sub02_04, name='SUB02_04'),
    path('sub02/sub02_05', sub02.sub02_05, name='SUB02_05'),

    path('sub03/sub03_01', sub03.sub03_01, name='SUB03_01'),
    path('sub03/sub03_02', sub03.sub03_02, name='SUB03_02'),
    path('sub03/sub03_03', sub03.sub03_03, name='SUB03_03'),
    path('sub03/sub03_04', sub03.sub03_04, name='SUB03_04'),
    path('sub03/sub03_05', sub03.sub03_05, name='SUB03_05'),
    path('sub03/sub03_06', sub03.sub03_06, name='SUB03_06'),

    path('sub04/sub04_01', sub04.sub04_01, name='SUB04_01'),
    path('sub04/sub04_02', sub04.sub04_02, name='SUB04_02'),
    path('sub04/sub04_03', sub04.sub04_03, name='SUB04_03'),
    path('sub04/sub04_04', sub04.sub04_04, name='SUB04_04'),

    path('sub05/sub05_01', sub05.sub05_01, name='SUB05_01'),
]
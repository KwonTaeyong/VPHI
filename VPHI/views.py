from django.shortcuts import render

# Create your views here.

def index(request):


    return render(request, 'VPHI/index.html')

def WareHouse(requset):

    return render(requset, 'VPHI/Stock/WareHouse.html')
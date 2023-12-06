from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'ventas/index.html')

def sesions(request):
    return render(request, 'ventas/sesion.html')

def panel(request):
    return render(request, 'panel.html')

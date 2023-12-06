from django.shortcuts import render

# Create your views here.

def landingpage(request):
    return render(request, "landingpage.html")

def iniciosesion(request):
    return render(request, "iniciosesion.html")

def registro(request):
    return render(request, "registros.html")
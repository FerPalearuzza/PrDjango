from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, "core/index.html")

def historia(request):
    return render(request, "core/historia.html")

def latte(request):
    return render(request, "core/latte.html")

def capuccino(request):
    return render(request, "core/capuccino.html")

def iceCoffe(request):
    return render(request, "core/iceCoffe.html")

def masReceta(request):
    return render(request, "core/masReceta.html")

def contacto(request):
    return render(request, "core/contacto.html")










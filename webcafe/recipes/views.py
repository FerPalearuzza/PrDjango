from django.shortcuts import render
from .models import Receta

# Create your views here.
def bdrecetas(request, entidad_id):
    rexeta = Receta.objects.get(pk=entidad_id)
    return render(request, "recipes/baserecipe.html",{'rexeta':rexeta})


def receta(request):
    rexetas = Receta.objects.all()
    return render(request, "recipes/receta.html",{'rexetas':rexetas})

# def bdrecetas(request):
#    rexeta = Receta.objects.all()
#    return render(request, "recipes/baserecipe.html",{'rexeta':rexeta})

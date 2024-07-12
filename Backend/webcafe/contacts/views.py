from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Contacto
import json

# Create your views here.

def tablecontactos(request):
    if request.method == 'POST':
        nombre = request.POST.get('name')
        correo = request.POST.get('email')
        tipoconsulta = request.POST.get('tipoConsulta')
        mensaje = request.POST.get('message')
        suscripto = request.POST.get('newsletter') == 'true'
        
        # if suscripto == "on":
        #     suscripto = True  # La casilla está marcada
        # else:
        #     suscripto = False  # La casilla no está marcada
        nuevocontacto = Contacto(fullname=nombre, email=correo, consulttype=tipoconsulta, comments=mensaje, bulletin=suscripto)
        nuevocontacto.save()
        data= {'nombre':nombre, 'email':correo, 'consultaTipo':tipoconsulta, 'comments':mensaje, 'bulletin':suscripto}
        print(data)
        #  nuevocontacto = Contacto.objects.create(fullname=nombre, email=correo, consulttype=tipoconsulta, comments=mensaje, bulletin=suscripto)
        return JsonResponse(data, safe=False)  # Cambia 'contact_success' por el nombre de tu vista de éxito
    else:
            
        return render(request, 'contacts/contacto.html',{})


def contacto(request):
    return render(request, "contacts/contacto.html")

from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
# Create your views here.

def index(request):
    return render(request, 'paginas/index.html')

def prueba(request):
    return render(request, 'paginas/prueba.html')

def saludo(request):
    #siempre preguntar con POST 
    if ('cajanombre' in request.POST):
        dato = request.POST['cajanombre']
        informacion = {
            'nombre':dato
        }
        return render(request, 'paginas/saludo.html', informacion)
    else:
        #nada
        return render(request, 'paginas/saludo.html')
    
def sumar(request):
    if ('cajanum1' in request.POST and 'cajanum2' in request.POST):
        dato1 = int(request.POST['cajanum1'])
        dato2 = int(request.POST['cajanum2'])
        suma = dato1+dato2
        informacion = {
            'suma':suma
        }
        return render(request, 'paginas/sumar.html', informacion)
    else:  
        return render(request, 'paginas/sumar.html')
    
def par(request):
    if ('num' in request.POST):
        dato1 = int(request.POST['num'])
        if dato1 % 2 == 0:
            resultad = 'par'
        else:
            resultad = 'impar'
        informacion = {
            'res':resultad
        }
        return render(request, 'paginas/par.html', informacion)
    else:  
        return render(request, 'paginas/par.html')
    
def colat(request):
    if ('num' in request.POST):
        lista = []
        numero = int(request.POST['num'])
        while (numero != 1):
            if numero % 2 == 0:
                numero = numero / 2
            else:
                numero = numero * 3 + 1
            lista.append(numero)
        informacion = {
            'res':lista 
        }
        return render(request, 'paginas/colat.html', informacion)
    else:  
        return render(request, 'paginas/colat.html')
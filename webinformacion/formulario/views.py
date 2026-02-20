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
    
def tabla(request):
    if ('num' in request.POST):
        numero = int(request.POST['num'])
        lista = []
        for n in range(1,11):
            res = numero * n 
            lista.append(res)
        info = {
            'listares':lista
        }
        return render(request, 'paginas/tabla.html', info)
    else:
        return render(request, 'paginas/tabla.html')
    
def deportes(request):
    listaDeportes = ['Futbol', 'Petanca', 'Curling', 'Dardos', 'Rana', 'Baloncesto', 'Snooker', 'Rugby']
    if ('selectdeporte' in request.POST):
        deporte = request.POST['selectdeporte']
        info = {
            'listadeportes':listaDeportes,
            'deporte':deporte
        }
        return render(request, 'paginas/deportes.html', info)
    else:
        info = {
            'listadeportes':listaDeportes
        }
        return render(request, 'paginas/deportes.html', info)
    
def color(request):
    listacoloreses = {
        'red':'Rojo', 
        'yellow':'Amarillo', 
        'green':'Verde', 
        'blue':'Azul'
        }
    if ('selectdeporte' in request.POST):
        color = request.POST['selectdeporte']
        info = {
            'listacolores':listacoloreses,
            'deporte':color,
            'coloress':listacoloreses[color]
        }
        return render(request, 'paginas/color.html', info)
    else:
        info = {
            'listacolores':listacoloreses
        }
        return render(request, 'paginas/color.html', info)
    
def comics(request):
    listacomics = [
        {
            "index": 0,
            "titulo": "Spiderman",
            "imagen": "https://elcoleccionistacomics.com/60266-medium_default/spiderman-de-todd-mcfarlane-vol1-de-6.jpg"
        },
        {
            "index": 1,
            "titulo": "Spawn",
            "imagen": "https://m.media-amazon.com/images/I/91hZO1pjAoL._AC_UF1000,1000_QL80_.jpg"
        },
        {
            "index": 2,
            "titulo": "Wolverine",
            "imagen": "https://www.kamekame.es/53918-large_default/marvel-omnibus-dinastia-de-x-potencias-de-x-comic.jpg"
        },
        {
            "index": 3,
            "titulo": "Wolverine",
            "imagen": "https://www.kamekame.es/53918-large_default/marvel-omnibus-dinastia-de-x-potencias-de-x-comic.jpg"
        },
        {
            "index": 4,
            "titulo": "Asterix y Obelix",
            "imagen": "https://comicsbarcelona.com/wp-content/uploads/2015/11/127913-Asterix-2.-La-Hoz-de-Oro.jpg"
        }
    ]
    if ('selectcomic' in request.POST):
        indice = int(request.POST['selectcomic'])
        comic = listacomics[indice]
        info = {
            'listacomics':listacomics,
            'comic':comic
        }
        return render(request, 'paginas/comics.html', info)
    else:
        info = {
            'listacomics':listacomics
        }
        return render(request, 'paginas/comics.html', info)
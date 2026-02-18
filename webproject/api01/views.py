from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'paginas/index.html')

def prueba(request):
    return render(request, 'paginas/prueba.html')

def peliculas(request):
    return  render(request, "paginas/peliculas.html")

def futbol(request):
    informacion = {
        'equipo':'Bilbao'
    }
    return render(request, 'paginas/futbol.html', informacion)

def nombres(request):
    lista = ['giorgi', 'david', 'alejandra', 'selena', 'ruby']
    listapersona = [
        {
            'nombre':'novaria',
            'edad':23
        },
        {
            'nombre':'selena',
            'edad':24
        },
        {
            'nombre':'martis',
            'edad':26
        },
        {
            'nombre':'ginever',
            'edad':21
        }
    ]
    informacion = {
        'listanombres': lista,
        'listapersona':listapersona
    }
    
    return render(request, 'paginas/nombres.html', informacion)

def mascotas(request):
    listamascotas = [
        {
            'nombre':'jeka',
            'raza':'perro',
            'edad':8
        },
        {
            'nombre':'bob',
            'raza':'gato',
            'edad':5
        },
        {
            'nombre':'susi',
            'raza':'vaca',
            'edad':5
        },
        {
            'nombre':'random',
            'raza':'serpiente',
            'edad':9
        },
        {
            'nombre':'jeka',
            'raza':'perro',
            'edad':8
        }
    ]
    info = {
        'lista':listamascotas
    }
    return render(request, 'paginas/mascotas.html', info)

def colores(request):
    if ('micolor' in request.GET):
        colorrecibido = request.GET['micolor']
    else:
        colorrecibido = "Nada"
    context = {
        'color':colorrecibido
    }
    return render(request, 'paginas/colores.html', context)
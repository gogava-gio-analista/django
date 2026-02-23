from django.shortcuts import render
from django.http import HttpResponse
from hospitales import models as md 
# Create your views here.

def index(request):
    return render(request, "index.html")

def tabladept(request):
    service = md.ServiceDepartamentos()
    lista = service.getDepartamentos()
    info = {
        'departamentos':lista
    }
    return render(request, 'departamentos.html', info)

def insertardept(request):
    if ('cajaid' in request.POST):
        service = md.ServiceDepartamentos()
        id = int(request.POST['cajaid'])
        nombre = request.POST['cajanombre']
        loc = request.POST['cajalocalidad']
        service.insertarDepartamento(id, nombre, loc)
        return render(request, 'insertardept.html')
    else:
        return render(request, 'insertardept.html')
    
def updatedept(request):
    if ('cajaid' in request.POST):
        service = md.ServiceDepartamentos()
        listaids = service.getDepartamentos()
        id = int(request.POST['cajaid'])
        nombre = request.POST['cajanombre']
        loc = request.POST['cajalocalidad']
        service.updatedept(id, nombre, loc)
        info = {
            'listaids':listaids
        }
        return render(request, 'updatedept.html', info)
    else:
        service = md.ServiceDepartamentos()
        listaids = service.getDepartamentos()
        info = {
            'listaids':listaids
        }
        return render(request, 'updatedept.html', info)
    
def buscardepartamentoform(request):
    if ('cajaid' in request.POST):
        service = md.ServiceDepartamentos()
        id = int(request.POST['cajaid'])
        dept = service.buscardept(id)
        info = {
            'departamento': dept
        }
        return render(request, 'buscarform.html', info)
    else:
        return render(request, 'buscarform.html')
    
def buscardepartamentosget(request):
    return render(request, 'buscarget.html')
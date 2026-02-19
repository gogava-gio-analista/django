from formulario import views
from django.urls import path

urlpatterns=[
    path('', views.index, name='index'),
    path('prueba/', views.prueba, name='prueba'),
    path('saludo/', views.saludo, name='saludo'),
    path('sumar/', views.sumar, name='sumar'),
    path('par/', views.par, name='par'),
    path('colat/', views.colat, name='colat'),
]
from django.urls import path
from api01 import views

urlpatterns=[
    path('prueba/', views.prueba, name='prueba'),
    path('index/', views.index, name='index'),
    path('peliculas/', views.peliculas, name='peliculas'),
    path('futbol/', views.futbol, name='futbol'),
    path('nombres/', views.nombres, name='nombres'),
    path('mascotas/', views.mascotas, name='mascotas'),
    path('colores/', views.colores, name='colores')
]

# Parámetros método path:
# Primero: Cuando se dirija a la url ‘’ (vacía).
# Segundo: Le diremos que vaya a index de view.
# Tercero: Nombre que le damos.
#path('prueba/', views.prueba, name='prueba')
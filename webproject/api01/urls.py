from django.urls import path
from api01 import views

urlpatterns=[
    path('prueba/', views.prueba, name='prueba'),
    path('index/', views.index, name='index')
]

# Parámetros método path:
# Primero: Cuando se dirija a la url ‘’ (vacía).
# Segundo: Le diremos que vaya a index de view.
# Tercero: Nombre que le damos.
#path('prueba/', views.prueba, name='prueba')
from django.urls import path
from practica import views

urlpatterns=[
    path('prueba/', views.prueba, name='prueba'),
    path('martes/', views.martes, name='martes'),
    path('miercoles/', views.miercoles, name='miercoles'),
    path('barcelona/', views.barcelona, name='barcelona'),
    path('madrid/', views.madrid, name='madrid')
]
from hospitales import views
from django.urls import path

urlpatterns=[
    path('', views.index, name='index'),
    path('departamentos/', views.tabladept, name='departamentos'),
    path('insertardept/', views.insertardept, name='insertardept'),
    path('updatedept/', views.updatedept, name='updatedept'),
    path('buscarform/', views.buscardepartamentoform, name='buscarform'),
    path('buscarget/', views.buscardepartamentosget, name='buscarget'),
]
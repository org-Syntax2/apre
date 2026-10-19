from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resultado/', views.resultado, name='resultado'),
    path('evacuacion/', views.evacuacion_view, name='evacuacion'), # <--- Agrega esta línea
]
from django.urls import path
from . import views

app_name = 'zapatos'

urlpatterns = [
    path('', views.index, name='index'),
    path('comprar/', views.comprar, name='comprar'),
    path('contacto/', views.contacto, name='contacto'),
    path('clima/', views.clima, name='clima'),
    path('registro/', views.registro, name='registro'),
    path('zapatillas/', views.zapatillas, name='zapatillas'),
    path('ingreso/', views.ingreso_view, name='ingreso'),
]

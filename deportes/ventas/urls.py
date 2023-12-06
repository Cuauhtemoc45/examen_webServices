# En el archivo urls.py de la aplicación
from django.urls import path
from . import views  # Importa las vistas de tu aplicación

urlpatterns = [
    path('', views.index, name='index'),  # Define una URL base, usando la vista 'index'
    path('ventas/sesion/', views.sesions, name='sesion'),
    path('panel/', views.panel, name='panel')
    
    
]

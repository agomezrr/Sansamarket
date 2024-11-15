from django.urls import path
from . import views

app_name = 'resenas'

urlpatterns = [
    path('crear/<int:usuario_id>/', views.crear_resena, name='crear_resena'),
    path('listar/<int:usuario_id>/', views.listar_resenas, name='listar_resenas'),
]
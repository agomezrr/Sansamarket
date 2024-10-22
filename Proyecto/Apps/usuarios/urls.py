from django.urls import path
from . import views


app_name = 'usuarios'

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.actualizar_perfil, name='perfil'),
    path('login/', views.login_view, name='login')
]
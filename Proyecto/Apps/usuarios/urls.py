from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'usuarios'

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.actualizar_perfil, name='perfil'),
    path('login/', views.login_view, name='login'),
    path('perfil/<int:pk>/', views.perfil_usuario, name='perfil'),
    path('', views.home, name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
]
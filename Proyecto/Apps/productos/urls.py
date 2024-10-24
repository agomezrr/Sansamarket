from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('explorar/', views.explorar_productos, name='explorar'),
    path('lista/', views.lista_productos, name='lista_productos'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('actualizar/<int:pk>/', views.actualizar_producto, name='actualizar_producto'),
    path('eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
    path('producto/<int:pk>/', views.detalle_producto, name='detalle_producto'),
]
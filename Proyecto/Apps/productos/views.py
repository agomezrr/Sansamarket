from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def explorar_productos(request):
    return render(request, 'productos/explorar.html')

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista_productos.html', {'productos': productos})

@login_required
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.usuario = request.user  # Asigna el usuario actual
            producto.save()
            return redirect('productos:lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'productos/agregar_producto.html', {'form': form})

@login_required
def actualizar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if producto.usuario != request.user:
        return redirect('productos:lista_productos')  # Redirigir si el usuario no es el propietario

    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos:lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/actualizar_producto.html', {'form': form})

@login_required
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if producto.usuario != request.user:
        return redirect('productos:lista_productos')  # Redirigir si el usuario no es el propietario

    if request.method == 'POST':
        producto.delete()
        return redirect('productos:lista_productos')
    return render(request, 'productos/eliminar_producto.html', {'producto': producto})

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'productos/detalle_producto.html', {'producto': producto})
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Resena
from .forms import ResenaForm
from django.contrib.auth.models import User

@login_required
def crear_resena(request, usuario_id):
    usuario = get_object_or_404(User, id=usuario_id)
    if request.method == 'POST':
        form = ResenaForm(request.POST)
        if form.is_valid():
            resena = form.save(commit=False)
            resena.usuario = usuario
            resena.calificador = request.user
            resena.save()
            return redirect('usuarios:perfil', pk=usuario.id)
    else:
        form = ResenaForm()
    return render(request, 'resenas/crear_resena.html', {'form': form, 'usuario': usuario})

def listar_resenas(request, usuario_id):
    usuario = get_object_or_404(User, id=usuario_id)
    resenas = Resena.objects.filter(usuario=usuario)
    return render(request, 'resenas/listar_resenas.html', {'resenas': resenas, 'usuario': usuario})


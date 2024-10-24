from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import RegistroForm
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from .forms import PerfilForm
from .forms import LoginForm, UserForm
from .models import Perfil
# Create your views here.

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('usuarios:perfil', pk=user.pk)  # Redirigir al perfil del usuario
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})

@login_required
def editar_perfil(request):
    user = request.user
    perfil = get_object_or_404(Perfil, user=user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        perfil_form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
            return redirect('usuarios:perfil', pk=user.pk)
    else:
        user_form = UserForm(instance=user)
        perfil_form = PerfilForm(instance=perfil)

    return render(request, 'usuarios/editar_perfil.html', {
        'user_form': user_form,
        'perfil_form': perfil_form
    })

def actualizar_perfil(request):
    perfil, created = Perfil.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('usuarios:perfil')
    else:
        form = PerfilForm(instance=perfil)
    
    return render(request, 'usuarios/perfil.html', {'form': form})

def home(request):
    return render(request, 'usuarios/home.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  
            else:
                messages.error(request, 'Credenciales incorrectas.')
    else:
        form = LoginForm()

    return render(request, 'usuarios/login.html', {'form': form})

def perfil_usuario(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    return render(request, 'usuarios/perfil_usuario.html', {'usuario': usuario})


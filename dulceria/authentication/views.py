from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistroUsuarioForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Has iniciado sesión como {username}.")
                return redirect("dashboard")
            else:
                messages.error(request, "Usuario o contraseña incorrectos.")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    form = AuthenticationForm()
    return render(request, "authentication/login.html", {"login_form": form})

def registro_view(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Cuenta creada exitosamente para: {username}. Ahora puedes iniciar sesión.")
            return redirect("login")
        else:
            messages.error(request, "Por favor corrige los errores del formulario.")
    else:
        form = RegistroUsuarioForm()
    return render(request, "authentication/registro.html", {"register_form": form})

@login_required
def dashboard_view(request):
    user = request.user
    context = {
        'user': user,
        'rol_nombre': user.id_rol.nombre if user.id_rol else 'Sin rol asignado'
    }
    
    # Determinar qué template mostrar según el rol
    if user.id_rol:
        if user.id_rol.nombre == "Operador de Bodega":
            return render(request, "dashboards/operador_bodega.html", context)
        elif user.id_rol.nombre == "Comprador":
            return render(request, "dashboards/comprador.html", context)
    
    # Dashboard por defecto si no tiene rol específico
    return render(request, "dashboard.html", context)
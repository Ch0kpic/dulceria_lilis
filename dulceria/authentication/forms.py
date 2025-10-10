from django import forms
from django.contrib.auth.forms import UserCreationForm
from usuarios.models import Usuario
from roles.models import Rol

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'tu@email.com'})
    )
    nombre = forms.CharField(
        max_length=150, 
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre completo'})
    )
    id_rol = forms.ModelChoiceField(
        queryset=Rol.objects.all(), 
        required=False, 
        empty_label="Selecciona un rol",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Excluir el rol de Administrador del formulario de registro
        self.fields['id_rol'].queryset = Rol.objects.exclude(
            nombre__icontains='Administrador'
        ).exclude(
            tipo='admin'
        )
        
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nombre de usuario'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Contraseña segura'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Repite la contraseña'})

    class Meta:
        model = Usuario
        fields = ("username", "email", "nombre", "id_rol", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.nombre = self.cleaned_data["nombre"]
        user.correo = self.cleaned_data["email"]
        if self.cleaned_data["id_rol"]:
            user.id_rol = self.cleaned_data["id_rol"]
        if commit:
            user.save()
        return user
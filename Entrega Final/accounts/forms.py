from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import forms
from django import forms
from django.core import validators
from django.contrib.auth.forms import PasswordChangeForm

class MiFormularioDeCreacion(UserCreationForm, forms.Form):
    
    username = forms.CharField(
        max_length=30,
        required=True,
        label = 'Nombre del usuario',
        widget=forms.TextInput(
            attrs={
                'placeholder' : 'Introduzca nombre de usuario '
                },
            ),
        error_messages={
            "unique": "El usuario existe en la base de datos."
        },
        validators=[
            validators.MinLengthValidator(2, 'El nombre de usuario es demasiado corto.'),
            validators.MaxLengthValidator(31, 'El nombre de usuario es demasiado largo.')
        ]
    )

    first_name = forms.CharField(
        max_length=30,
        required=False,
        label = 'Nombre',
        widget=forms.TextInput(
            attrs={
                'placeholder' : 'Introduzca su nombre '
                },
            )
        )
    last_name = forms.CharField(
        max_length=30,
        required=False,
        label = 'Apellido',
        widget=forms.TextInput(
            attrs={
                'placeholder' : 'Introduzca su apellido'
                },
        )
    )

    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder' : 'Introduzca su correo electrónico '
                }
            )
   )
    
    password1 = forms.CharField(
        label='Contraseña', 
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Repetir Contraseña', 
        widget=forms.PasswordInput
    )
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {key: '' for key in fields}
        
class EditarPerfilFormulario(forms.Form):
    username = forms.CharField(
        label='Usuario',
        required=True,
        validators=[
            validators.MinLengthValidator(2, 'El nombre de usuario es demasiado corto.'),
            validators.MaxLengthValidator(31, 'El nombre es demasiado Largo.')
        ]
    ) 
    first_name = forms.CharField(
        label='Nombre',
        required=False,
        validators=[
            validators.MinLengthValidator(2, 'El nombre es demasiado corto.'),
            validators.MaxLengthValidator(31, 'El nombre es demasiado Largo.')
        ]
    )
    last_name = forms.CharField(
        label='Apellido',
        required=False,
        validators=[
            validators.MinLengthValidator(2, 'El nombre de usuario es demasiado corto.'),
            validators.MaxLengthValidator(31, 'El nombre es demasiado Largo.')
        ]
    )
    email = forms.CharField(
        label='Email',
        required=True
    )
    descripcion = forms.CharField(
        label='Descripcion',
        required=False,
        validators=[
            validators.MaxLengthValidator(100, 'descripción demasiado larga')
        ]
    )
    avatar = forms.ImageField(required=False, error_messages = {'invalid': "Solo imágenes"}, widget=forms.FileInput)
    

class MiCambioDePassword(PasswordChangeForm):
    old_password = forms.CharField(label='Contraseña vieja', widget=forms.PasswordInput) 
    new_password1 = forms.CharField(label='Contraseña nueva', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Repetir Contraseña nueva', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        help_texts = {key: '' for key in fields}
    

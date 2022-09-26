from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppMundial.models import Avatar, Posts
from ckeditor.fields import RichTextFormField
from ckeditor.widgets import CKEditorWidget



class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput) 

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email']

class AvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ['imagen']

class PosteoFormulario(forms.Form):
    titulo=forms.CharField(max_length=120)
    equipo=forms.CharField(max_length=120)
    posteo=forms.CharField(widget = CKEditorWidget())
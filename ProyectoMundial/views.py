from re import U
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context, loader
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm 
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView, LoginView
from AppMundial.forms import UserRegisterForm, UserUpdateForm, AvatarFormulario, PosteoFormulario
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

#Vistas de Usuarios

def register(request):
    mensaje = ''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "02-home.html", {"mensaje":"Usuario creado con exito :"})
        else:
            mensaje = 'Cometiste un error en el registro'
    formulario = UserRegisterForm()  # Formulario vacio para construir el html
    context = {
        'form': formulario,
        'mensaje': mensaje
    }
    return render(request, "06-0-registro.html", context=context)

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('home')
    template_name = '07-0-form_perfil.html'

    def get_object(self, queryset=None):
        return self.request.user

def agregar_avatar(request):
    if request.method == 'POST':

        form = AvatarFormulario(request.POST, request.FILES) #aquí me llega toda la información del html

        if form.is_valid:   #Si pasó la validación de Django
            avatar = form.save()
            avatar.user = request.user
            avatar.save()
            return redirect(reverse('home'))

    form = AvatarFormulario() #Formulario vacio para construir el html
    return render(request, "AppMundial/07-1-form_avatar.html", {"form":form})

def login_request(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contra)
            if user:
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)
                return render(request, "02-home.html", {"mensaje":f"¡Hola {usuario}!"})
            else:
                return render(request,"02-home.html", {"mensaje":"Error, datos incorrectos"})
        else:
            return render(request,"02-home.html", {"mensaje":"Error, formulario erroneo"})

    form = AuthenticationForm()
    return render(request,"06-1-login.html", {'form':form} )

class Logout(LogoutView):
    template_name = '06-2-logout.html'
    

# Views de Pestañas

def home(request):
    return render(request, "02-home.html")

def selecciones(request):
    return render(request, "04-selecciones.html")

def estadios(request):
    return render(request, "05-estadios.html")

def integrantes(request):
    return render(request, "08-about_us.html")

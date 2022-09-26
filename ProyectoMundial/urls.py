"""ProyectoMundial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from xml.dom.minidom import Document
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from ProyectoMundial.views import login_request, register,  agregar_avatar, ProfileUpdateView,  estadios, selecciones, home, Logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('proyecto-mundial/', include('AppMundial.urls')),
    #Registro usuario y sesion
    path('login/', login_request, name = 'login'),
    # path('login/', views.CustomLoginView.as_view, name = 'login'),
    path('login/register/', register, name = 'register'),
    path('logout/', Logout.as_view(), name='logout'),
    # URLS Perfil
    path('editar-perfil/', ProfileUpdateView.as_view(), name="editar_perfil"),
    path('agregar-avatar/', agregar_avatar, name="agregar_avatar"),
    #Pestaña Principal
    path('', home, name="home"),
    path('selecciones/', selecciones, name="selecciones"),
    path('estadios/', estadios, name="estadios"),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
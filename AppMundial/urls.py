from django.urls import path
from AppMundial import views

urlpatterns = [
#Registro usuario y sesion
    path('login/', views.login_request, name = 'login'),
    # path('login/', views.CustomLoginView.as_view, name = 'login'),
    path('login/register/', views.register, name = 'register'),
    path('logout/', views.CustomLogoutView.as_view(), name = 'logout'),
# URLS Perfil
    path('editar-perfil/', views.ProfileUpdateView.as_view(), name="editar_perfil"),
    path('agregar-avatar/', views.agregar_avatar, name="agregar_avatar"),
    #Pestaña Principal
    path('', views.home, name="home"),
    path('blog/', views.blog, name="blog"),
    path('selecciones/', views.selecciones, name="selecciones"),
    path('estadios/', views.estadios, name="estadios"),
]
from django.urls import path
from . import views
#URLS para el Blog
urlpatterns = [
    path('blog/', views.PostList.as_view(), name='blog'),
    path('nuevo/', views.CreatePost.as_view(), name='New'),
    path('<pk>/', views.PostDetails.as_view(), name='Detail'),
    path('editar/<pk>/', views.ModifyPost.as_view(), name='post_Edit'),
    path('borrar/<pk>/', views.DeletePost.as_view(), name='post_Delete'),
]
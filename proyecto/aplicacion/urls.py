from django.urls import path
from . import views

urlpatterns = [
    path('', views.usuario_list, name='usuario_list'),
    path('adicionar/', views.usuario_add, name='usuario_add'),
    path('editar/<int:pk>/', views.usuario_edit, name='usuario_edit'),
    path('borrar/<int:pk>/', views.usuario_delete, name='usuario_delete'),
    path('tipo_list/', views.tipo_de_usuario_list, name='tipo_usuario_list'),
    path('tipo_adicionar/', views.tipo_de_usuario_add, name='tipo_usuario_add'),
    path('tipo_editar/<int:pk>/', views.tipo_de_usuario_edit, name='tipo_usuario_edit'),
    path('tipo_borrar/<int:pk>/', views.tipo_de_usuario_delete, name='tipo_usuario_delete'),
]

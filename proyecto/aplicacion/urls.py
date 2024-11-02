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
    path('tipo_de_plan/', views.tipo_de_plan_list, name='tipo_plan_list'),
    path('tipo_plan_adicionar/', views.tipo_de_plan_add, name='tipo_plan_add'),
    path('tipo_plan_editar/<int:pk>/', views.tipo_de_plan_edit, name='tipo_plan_edit'),
    path('tipo_plan_borrar/<int:pk>/', views.tipo_de_plan_delete, name='tipo_plan_delete'),
    path('pago/', views.pago_list, name='pago_list'),
    path('pago_adicionar/', views.pago_add, name='pago_add'),
    path('pago_editar/<int:pk>/', views.pago_edit, name='pago_edit'),
    path('pago_borrar/<int:pk>/', views.pago_delete, name='pago_delete'),

]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('create_account/',views.create_account , name='occount'),
    path('admins/', views.administrador, name='administrador'),
    path('client/', views.cliente, name='cliente'),


]
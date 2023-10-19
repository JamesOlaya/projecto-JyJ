from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('create_account/',views.create_account , name='occount'),
    path('admins/', views.administrador, name='administrador'),
    path('cliente/', views.cliente, name='cliente'),
    path('user/', views.usuario, name='usuario'),
]


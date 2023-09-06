from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('create_occount', views.create_account, name='occount'),
    path('recover_password', views.recovery_password, name='recover')

]
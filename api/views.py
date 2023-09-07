from django.shortcuts import render,redirect
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login/login.html')

def create_account(request):
    return render(request,'create_account/create_account.html')

def recovery_password(request):
    return render (request, 'recover/recover.html')




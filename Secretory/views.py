from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'dashboard.html')

def signin(request):
    return render(request,'sign-in.html')

def signup(request):
    return render(request,'sign-up.html')
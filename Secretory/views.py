from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'dashboard.html')

def signin(request):
    return render(request,'sign-in.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['cpassword']:
            
            return render(request,'sign-up.html')
            
        return render(request,'sign-up.html',{'msg':'Both pass are not same'})


    return render(request,'sign-up.html')
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def index(request):
    return render(request,'dashboard.html')

def signin(request):
    try:
        user = Secratory.objects.get(email=request.session['email'])
        return render(request,'dashboard.html',{'user':user})
    except:
        if request.method == 'POST':
            try:
                user = Secratory.objects.get(email=request.POST['email'])
                if request.POST['password'] == user.password:
                    request.session['email'] = user.email

                    return render(request,'dashboard.html',{'user':user})
                return render(request,'sign-in.html',{'msg':'Incorrect Password'})
            except:
                return render(request,'sign-up.html',{'msg':'Account does not exist please sign up first!!'})
        return render(request,'sign-in.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['cpassword']:
            try:
                Secratory.objects.get(email=request.POST['email'])
                return render(request,'sign-in.html',{'msg':'Account alreadt exist please sign in'})
            except:
                Secratory.objects.create(
                    name = request.POST['name'],
                    email = request.POST['email'],
                    mobile = request.POST['mobile'],
                    address = request.POST['address'],
                    password = request.POST['password']
                )

            return render(request,'sign-in.html',{'msg':'Account created go and sign in'})
            
        return render(request,'sign-up.html',{'msg':'Both pass are not same'})


    return render(request,'sign-up.html')

def logout(request):
    del request.session['email']
    return redirect('signin')

def change_password(request):
    try: 
        user = Secratory.objects.get(email=request.session['email'])
        if request.POST:
            if request.POST['opassword'] == user.password:
                if request.POST['npassword'] == request.POST['cpassword']:
                    user.password = request.POST['npassword']
                    user.save()
                    return render(request,'change-password.html',{'msg':'Password Updated','user':user})
                return render(request,'change-password.html',{'msg':'New passwords are not matching','user':user})
            return render(request,'change-password.html',{'msg':'Old password incorrect','user':user})
        return render(request,'change-password.html',{'user':user})
    except:
        return render(request,'sign-in.html',{'msg':"Sign in first"})
    

def edit_profile(request):
    try:
        user = Secratory.objects.get(email=request.session['email'])
        if request.method == 'POST':
            user.name = request.POST['name']
            user.mobile = request.POST['mobile']
            user.address = request.POST['address']
            if 'pic' in request.FILES:
                user.profile_pic = request.FILES['pic']
            user.save()
        return render(request,'edit-profile.html',{'user':user})
    except:
        return render(request,'sign-in.html')
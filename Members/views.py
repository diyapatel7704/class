from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def member_index(request):
    return render(request,'member-index.html')

def member_login(request):
    try:
        user = Member.objects.get(email=request.session['memail'])
        return render(request,'member-index.html',{'user':user})
    except:
        if request.method == 'POST':
            # try:
                user = Member.objects.get(email=request.POST['email'])
                if user.password == request.POST['password']:
                    request.session['memail'] = user.email
                    return redirect('member-index')
                return render(request,'member-login.html',{'msg':'Password is incorrect'})
            # except:
            #     return render(request,'member-login.html',{'msg':'Account not found'})
        
        return render(request,'member-login.html')

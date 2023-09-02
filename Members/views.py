from django.shortcuts import render, redirect
from .models import *
from Secretory import models
from datetime import date

# Create your views here.

def member_index(request):
    events = models.Event.objects.filter(date__gte = str(date.today()) )[::-1]
    event_count = models.Event.objects.all().count()
    return render(request,'member-index.html',{
        'events':events , 
        'event_count':event_count
        })

def member_login(request):
    try:
        user = Member.objects.get(email=request.session['memail'])
        return render(request,'member-index.html',{'user':user})
    except:
        if request.method == 'POST':
            try:
                user = Member.objects.get(email=request.POST['email'])
                if user.password == request.POST['password'] and user.verify:
                    request.session['memail'] = user.email
                    return redirect('member-index')
                return render(request,'member-login.html',{'msg':'Password is incorrect'})
            except:
                return render(request,'member-login.html',{'msg':'Account not found'})
        
        return render(request,'member-login.html')


def member_logout(request):
    del request.session['memail']
    return redirect('member-index')


def create_complain(request):
    if request.POST:
        user = Member.objects.get(email=request.session['memail'])
        models.Complain.objects.create(
            complain_by = user,
            subject = request.POST['subject'],
            des = request.POST['des'],
            pic = request.FILES['pic'] if request.FILES else None
        )

        return render(request,'create-complain.html',{'msg':'Complain has been registered'})
    return render(request,'create-complain.html')
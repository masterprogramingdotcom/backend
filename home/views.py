from django.shortcuts import render,redirect
from django.contrib import messages
from home.models import *
# Create your views here.

def home(request):    
    if request.method == 'POST':
        data = request.POST
        enq = Enquire(
            name = data['name'],
            email = data['email'],
            number = data['number'],
            city = data['city'],
            program = data['program']
        )
        messages.success(request,"Successfully Submit")
        enq.save()

        return redirect('/')
    return render(request,'home/index.html')


def about(request):
    return render(request,'home/about.html')

def services(request):
    if request.method == 'POST':
        data = request.POST
        enq = Enquire(
            name = data['name'],
            email = data['email'],
            number = data['number'],
        )
        messages.success(request,"Successfully Submit")
        enq.save()
        
    return render(request,'home/services.html')

def contact(request):
    if request.method == 'POST':
        data = request.POST
        enq = Enquire(
            name = data['name'],
            email = data['email'],
            number = data['number'],
        )
        messages.success(request,"Successfully Submit")
        enq.save()
        
    return render(request,'home/contact.html')

def kyrgyzstan(request):
    return render(request,'country/kyrgyzstan.html')


def kazakhstan(request):
    return render(request,'country/kazakhstan.html')



def barbados(request):
    return render(request,'country/barbados.html')

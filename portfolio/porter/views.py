#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from porter.models import contact

# Create your views here.


# Types of views in python Django:- Function-Based & class-based view

#Function Based:- A python function that takes a web request and returns a web response.
#class based:- They provide an object-oriented way of organising your view code.

# Function Based view:
def index(request):
    return render(request,'index.html')
# return HttpResponse('Hello, Mate! This is Index Page')

#class based view:
from django.views import View

def about(request):
    return render(request, 'about.html')
    # return HttpResponse('This is About Page.')
    
def skills(request):
    return render(request,'skills.html')
    # return HttpResponse('This is About My Skills!')   

def certifications(request):
    return render(request,'certifications.html')
    # return HttpResponse('This is About My Certifications!')

def qualifications(request):
    return render(request,'qualifications.html')
    # return HttpResponse('This is About My Qualifications!')

def projects(request):
    return render(request,'projects.html')
    # return HttpResponse('This is About My Projects ')

def contact(request):
    if request.method== "POST":
        Name=request.POST.get('Name')
        Email=request.POST.get('email')
        Phone=request.POST.get('phone')
        Message=request.POST.get('message')
        contact =contact(Name=Name,Email=Email,Phone=Phone,Message=Message)
    return render(request,'contact.html')    
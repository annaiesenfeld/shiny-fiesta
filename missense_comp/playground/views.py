from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request): 
    return HttpResponse('Welcome to Missense3D-Intereact')
    #we need to map the request to a URL 
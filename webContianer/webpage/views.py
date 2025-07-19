from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home (request):
    return render(request,"home.html")

def login (request):
    return render(request,"login.html")

def register(request):
    return render(request,"register.html")

def infomation(request):
    return render(request,"infomation.html")

def production(request):
    return render(request,"production.html")


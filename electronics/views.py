from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("HOME")
def index(request):
    return HttpResponse("Hello World!")
def aboutus(request):
    return render(request, 'electronics/aboutus.html')
def homepage(request):
    return render(request, 'electronics/homepage.html')
def contactus(request):
    return render(request, 'electronics/contactus.html')
def login(request):
    return render(request, 'electronics/login.html')
def register(request):
    return render(request,'electronics/register.html')

from django.shortcuts import render, redirect
from.models import bureaucrat
from.forms import bureaucratform

# Create your views here.
def addbureaucrat(request):
    Bureaucrat= bureaucrat( pName="Prayash",pSurname="Shah", Dateofbirth="2001-09-18",Exam="UPSC-CSE",joiningDate="2024-02-12")
    Bureaucrat.save()
    print ("Data saved")
    return render(request,'bureaucrat/addbureaucrat.html')

def addbureaucratwithform(request):

    form = bureaucratform()
    if request.method == 'POST':
        form=bureaucratform(request.POST or None)
        if form.is_valid():
            form.save()

    return render(request,'bureaucrat/bureaucratform.html',{'form':form})

def updatebureaucratwithform(request,id):
    Bureaucrat = bureaucrat.objects.get(id=id)
    form=bureaucratform()
    print("post update")

    form = bureaucratform(request.POST or None,instance=Bureaucrat)
    if form.is_valid():
        form.save()

    return render(request, 'bureaucrat/bureaucrtupdate.html',{'form':form})







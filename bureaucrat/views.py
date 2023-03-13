from django.shortcuts import render, redirect
from.models import bureaucrat
from.forms import bureaucratform
from django.http import HttpResponse

# Create your views here
def getallbureaucrat(request):
    Bureaucrat= bureaucrat.objects.all().values()
    print(Bureaucrat)
    return render(request,'bureaucrat/allbureaucrat.html',{'bureaucrat':Bureaucrat})


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
        return redirect('getallbureaucrat')

    return render(request, 'bureaucrat/bureaucratupdate.html',{'form':form})

def deletebureaucrat(request, id ):
    Bureaucrat = bureaucrat.objects.get(id=id)
    Bureaucrat.delete()
    return redirect('getallbureaucrat') 
    return HttpResponse("bureaucrat deleted")
    #return render(request,'bureaucrat/deletebureaucrat.html')

def bureaucratdetails(request, id):
    Bureaucrat=bureaucrat.objects.get(id=id)
    return render(request, 'bureaucrat/bureaucratdetails.html',{'bureaucrat':Bureaucrat})








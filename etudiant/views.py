from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse, get_object_or_404
from .forms import StudentrRegistration
from .models import LoginInfo

# Create your views here.
def add(request):
    print(request.method)
    if request.method == 'POST':
        myform=StudentrRegistration(request.POST)
        print(myform)
        if myform.is_valid():
            myform.save()
            myform=StudentrRegistration()
            
            #print("la data est :  ", data)
            
            
    else: 
        myform=StudentrRegistration()
        
            
    return render(request, "etudiant/add.html", {'myform':myform})

def show(request):
    data=LoginInfo.objects.all()
    return render(request, 'etudiant/show.html', {"data":data})

def supp(request, id):
    
    #if request.method == "POST":
    pi=LoginInfo.objects.filter(id=id)
    pi.delete()
    all=pi=LoginInfo.objects.all()
    
    return render(request, 'etudiant/supp.html', {"data":all})

def modifier(request, id):
    article=LoginInfo.objects.get(id=id)

    #article=get_object_or_404(LoginInfo, id=id)
    form = StudentrRegistration( instance=article)
    return render(request, 'etudiant/modifier.html', {'form':form })

def update(request,id):
    #article=get_object_or_404(LoginInfo, id=id)
    article=LoginInfo.objects.get(id=id)
    if request.method=='POST':
        form = StudentrRegistration(request.POST, instance=article)
        if form.is_valid():
            form.save()
    else:
        form = StudentrRegistration(instance=article)
    return render(request, 'etudiant/show.html', {'form':form})

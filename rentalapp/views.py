from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Property
from .forms import PropertyForm

# Create your views here.
def home(request):
    properties = Property.objects.all()
    return render(request,'home.html',{'properties':properties})

def create(request):
    form = PropertyForm()
    if request.method == 'POST':
        print(request.POST)
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'create.html',{'form':form})

def update(request,id):
    property = Property.objects.get(id=id)
    form = PropertyForm(instance = property)
    if request.method == 'POST':
        print(request.POST)
        form = PropertyForm(request.POST,instance=property)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'create.html',{'form':form})

 
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Property,Profile
from .forms import PropertyForm

# Create your views here.
def home(request):
    properties = Property.objects.all()
    return render(request,'home.html',{'properties':properties})

def create(request):
    form = PropertyForm()
    if request.method == 'POST':
        print(request.POST)
        form = PropertyForm(request.POST,request.FILES)
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

def delete(request,id):
    property = Property.objects.get(id=id)
    property.delete()
    return redirect('home')

def details(request,id):
    property = Property.objects.get(id=id)
    return render(request,'details.html',{'property':property})

def register(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        middlename = request.POST.get('middlename')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2',default=password1)
        contact = request.POST.get('contact')
        profile = Profile(firstname=firstname,
                          lastname=lastname,
                          middlename=middlename,
                          username=username,
                          password1=password1,
                          password2=password2,
                          contact=contact)
        profile.save()
        return redirect('home')
    return render(request,'register.html',)

 
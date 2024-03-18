from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Property
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import PropertyForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    try:
        properties = Property.objects.filter(user=request.user)
    except: 
        properties = []
    return render(request,'home.html',{'properties':properties})

@login_required(login_url='login')
def create(request):
    form = PropertyForm()
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property = form.save(commit=False)
            if request.user.is_authenticated:  
                property.user = request.user  
                form.save()
                return redirect('home')
            else:
                return HttpResponse("You must be logged in to create a property.")
    return render(request, 'create.html', {'form': form})

def update(request,id):
    property = Property.objects.get(id=id)
    form = PropertyForm(instance = property)
    if (property.user == request.user):
        print(property.user)
        print(request.user)
        if request.method == 'POST':
            print(request.POST)
            form = PropertyForm(request.POST,request.FILES,instance=property)
            if form.is_valid():
                form.save()
                return redirect('home')
        return render(request,'create.html',{'form':form})
    else:
        return HttpResponse("Arkako update garchhas lathuwa")

def delete(request,id):
    property = Property.objects.get(id=id)
    property.delete()
    return redirect('home')

def details(request,id):
    property = Property.objects.get(id=id)
    return render(request,'details.html',{'property':property})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        User.objects.create_user(username=username,
                                 password=password,
                                 email=email)
        return redirect('home')
    return render(request,'register.html')

def loginn(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,
                            password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('home')
    return render(request,'login.html')

def logoutt(request):
    logout(request)
    return redirect('home')



 
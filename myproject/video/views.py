from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm


from  .models import Video
from  .forms import LoginForm

# Create your views here.

def home(request):
    last_video = Video.objects.all().order_by("-id")[0]
    return render(request,'home.html',{'last_video' : last_video})

def login(request):

    if request.method =='POST':
        form = LoginForm(request.POST)
        user = form.authenticate()
        if user:
            return redirect("/home")
        else:
            return HttpResponse('Form is not valid')

    else:
        form = LoginForm()
        return render(request,'login.html',{'form': form})

def register(request):
    print("call hocce")
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print("user form paice")
            if user:
                return  HttpResponse("User ID: " + str(user.id) + " created")
                print("user er account hoice")
            else:
                return  HttpResponse("ERROR")
                print("user error")
    else:
        form = UserCreationForm()
        print("user kicchu hoy nai")
    return render(request,'register.html',{'form':form})

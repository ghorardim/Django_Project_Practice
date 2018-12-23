from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib.auth import authenticate
from  .models import Video

# Create your views here.

def home(request):
    last_video = Video.objects.all().order_by("-id")[0]
    return render(request,'home.html',{'last_video' : last_video})

def login(request):

    if request.method =="POST":
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)

        if username is not None and password is not None and username != '' and password != '':
            user = authenticate(username = username, password = password)
            if user:
                return redirect("/")
            else:
                return HttpResponse("Login Field")
        else:
            return  HttpResponse("Empty Value Detectated")
    return render(request,'login.html')

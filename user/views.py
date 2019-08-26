from django.shortcuts import render,redirect
from .forms import LoginForm,RegisterForm
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User 
from django.contrib import messages
# Create your views here.

def LoginUser(request):
    form=LoginForm(request.POST or None)
    context={
        "form":form
    }
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user=authenticate(username=username,password=password)
        if user is None:
            messages.info(request,"Kullanıcı adı veya parola yanlış")
            return render(request,"login.html",context)
        messages.success(request,"Başarılı bir şekilde giriş yaptınız.")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)
def LogoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız")
    return redirect("index")
def register(request):
    form=RegisterForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        newUser=User(username=username)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        messages.success(request,"Başarılı bir şekilde kayıt oldunuz")
        return redirect("index")
    context={
        "form":form
    }
    return render(request,"register.html",context)
from django.shortcuts import render,redirect
from .models import Article
from .forms import ArticleForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    articles=Article.objects.all()
    context={
        "articles":articles
    }
    return render(request,"index.html",context)
@login_required(login_url = "user:login")
def dashboard(request):
    articles=Article.objects.filter(author=request.user)
    context={
        "articles":articles
    }

    return render(request,"dashboard.html",context)
@login_required(login_url = "user:login")
def addarticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Video  başarıyla oluşturuldu")
        return redirect("article:dashboard")
    return render(request,"addarticle.html",{"form":form})

def detail(request):
    return render(request,"detail.html")
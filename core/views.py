from django.shortcuts import render
from django.utils import timezone
from .models import Post

def core(request):
	posts = Post.objects.all()
	return render(request, 'core/core.html',{'posts': posts}) 

def porcoes(request):
	posts = Post.objects.all()
	return render(request, 'core/porcoes.html', {'posts': posts})

def pasteis(request):
	posts = Post.objects.all()
	return render(request, 'core/pasteis.html', {'posts': posts})

def hotdog(request):
	posts = Post.objects.all()
	return render(request, 'core/hotdog.html', {'posts': posts})

def refrigerante(request):
	posts = Post.objects.all()
	return render(request, 'core/refrigerante.html', {'posts': posts})

def cerveja(request):
	posts = Post.objects.all()
	return render(request, 'core/cerveja.html', {'posts': posts})

def coqueteis(request):
	posts = Post.objects.all()
	return render(request, 'core/coqueteis.html', {'posts': posts})
# Create your views here.

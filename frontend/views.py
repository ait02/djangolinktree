from .forms import LinkForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Link
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'frontend/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    
    context = {
        'form': form
    }
    return render(request, 'frontend/register.html', context)

def myLinks(request, username):
    user = User.objects.get(username=username)
    if user is not None:
        links = Link.objects.filter(owner=user)
        username = user.username
        if request.method == 'POST':
            form = LinkForm(request.POST)
            if form.is_valid():
                link = form.save(commit=False)
                link.owner = user
                link.save()
        else:
            form = LinkForm()
    else:
        links = []
        username = None
        return redirect('index')

    context = {
        'links': links,
        'username': username,
        'form': form,
    }
    return render(request, 'frontend/links.html', context)

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.template import loader
from .models import *
from .forms import mainForm, CreateUserForm
from .filters import mainFilter
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def registerPage(request):
    if  request.user.is_authenticated:
        return redirect('gallery')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account created for ' + user)
                return redirect('login')
        context= {
            'form': form
        }
        return render(request, 'Signal/register.html', context)

def loginPage(request):
    if  request.user.is_authenticated:
        return redirect('gallery')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('gallery')
            else:
                messages.info(request,'Username or password is incorrect.')
        context= {}
        return render(request, 'Signal/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def gallery_view(request):
    all_objects = Signal.objects.all()
    myFilter = mainFilter(request.GET, queryset=all_objects)
    all_objects = myFilter.qs
    context = {
        'all_objects': all_objects,
        'myFilter': myFilter
    }
    return render(request, 'Signal/gallery.html', context)

@login_required(login_url='login')
def list_view(request):
    all_objects = Category.objects.all()
    myFilter = mainFilter(request.GET, queryset=all_objects)
    all_objects = myFilter.qs
    context = {
        'all_objects': all_objects,
        'myFilter': myFilter
    }
    return render(request, 'Signal/list.html', context)

@login_required(login_url='login')
def table_view(request):
    all_objects = Signal.objects.all()
    myFilter = mainFilter(request.GET, queryset=all_objects)
    all_objects = myFilter.qs
    context = {
        'all_objects': all_objects,
        'myFilter': myFilter
    }
    return render(request, 'Signal/table.html', context)

@login_required(login_url='login')
def add(request):
    form = mainForm()
    if request.method == 'POST':
        form = mainForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = mainForm()
            return redirect('gallery')
    context = {
        'form': form
    }
    return render(request, 'Signal/add.html', context)

@login_required(login_url='login')
def view(request, id):
    instance = Signal.objects.get(id=id)
    myFilter = mainFilter(request.GET, queryset=instance)
    instance = myFilter.qs
    context = {
        'instance': instance,
        'myFilter': myFilter
    }
    return render(request, 'Signal/table.html', context)

@login_required(login_url='login')
def update(request,id):
    instance = Signal.objects.get(id=id)
    form = mainForm(instance=instance)
    if request.method == 'POST':
        form = mainForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            form = mainForm()
            return redirect('gallery')
    context = {
        'form': form
    }
    return render(request, 'Signal/add.html', context)

@login_required(login_url='login')
def delete(request,id):
    instance = Signal.objects.get(id=id)
    if request.method == 'POST':
        instance.delete()
        return redirect('gallery')
    context={
        'item':instance
    }
    return render(request, 'Signal/delete.html',context)


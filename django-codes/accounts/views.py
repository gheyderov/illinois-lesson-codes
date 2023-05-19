from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login as django_login, authenticate, logout as django_logout
from django.contrib import messages

# Create your views here.


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request=request, username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            if not user:
                messages.add_message(request, messages.ERROR, "User not found!")
            django_login(request, user)
            return redirect(reverse_lazy('home'))

    context = {
        'form' : form
    }
    return render(request, 'login.html', context)

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(data = request.POST, files=request.FILES)
        if form.is_valid():
            form.save(commit=False)
            return redirect('home')
    context = {
        'form' : form
    }
    return render(request, 'register.html', context)

def forget_password(request):
    return render(request, 'forget_password.html')

def profile(request):
    return render(request, 'user-profile.html')

def logout(request):
    django_logout(request)
    return redirect('login')
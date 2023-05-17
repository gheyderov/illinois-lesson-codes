from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def forget_password(request):
    return render(request, 'forget_password.html')

def profile(request):
    return render(request, 'user-profile.html')
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data= request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "SUCCESS")
            return redirect(reverse_lazy('contact'))
    context = {
        'form' : form
    }

    return render(request, 'contact.html', context)
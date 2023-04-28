from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import Signup
from django.http import HttpResponse

def index(request):
    items = Item.objects.filter(is_sold = False)[0:100]
    categories = Category.objects.all()
    return render(request, 'core/index.html',{
        'categories': categories,
        'Items': items,
    })
def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = Signup(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:    
        form = Signup()
    return render(request, 'core/signup.html',{
        'form':form
    })

def say_hello(request):
    text = """dear User :) Welcome to OODY Custom shop"""
    return render(request, 'core/sayhello.html')

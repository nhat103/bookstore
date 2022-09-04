from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, 'book/login.html')


def signup(request):
    return render(request, 'book/register.html')


def home(request):
    return render(request, 'book/home.html')


def viewcart(request):
    return render(request, 'book/viewcart.html')


def logout(request):
    return render(request, 'book/home.html')

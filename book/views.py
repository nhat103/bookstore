from django.shortcuts import render

# Create your views here.


def signin(request):
    return render(request, 'book/login.html')


def signup(request):
    if request.method == 'POST':
        usermame = request.POST['username']
        password = request.POST['password']
    else:
        return render(request, 'book/register.html')


def home(request):
    return render(request, 'book/home.html')


def viewcart(request):
    return render(request, 'book/viewcart.html')


def logout(request):
    return render(request, 'book/home.html')

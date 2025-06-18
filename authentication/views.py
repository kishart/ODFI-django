from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# Create your views here.

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, "authentication/signup.html")

        myuser = User.objects.create_user(username=username, email=email, password=password)
        myuser.first_name = name
        myuser.save()

        messages.success(request, "Your account has been created successfully!")
        return redirect("signin")
    else:
        return render(request, "authentication/signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            name = user.first_name
            return render(request, "authentication/index.html", {'name':name})
        else:
            messages.error(request, "Bad Credentials!")
            return redirect('uhome')
    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('home')


def uhome(request):
      return render(request, "authentication/user/uhome.html")


def home(request):
      return render(request, "authentication/index.html")

def about(request):
      return render(request, "authentication/user/about.html")

def gallery(request):
      return render(request, "authentication/user/gallery.html")

def contact(request):
      return render(request, "authentication/user/contact.html")

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import PhotoForm
from .models import Photo
from django.shortcuts import get_object_or_404

def delete_photo(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    if request.method == 'POST':
        photo.delete()
        return redirect('ahighlights')

def edit_photo(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('ahighlights')
    else:
        form = PhotoForm(instance=photo)
    return render(request, 'authentication/admin/edithighlights.html', {'form': form})


def ahighlights(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ahighlights')
        else:
            photos = Photo.objects.all()
            return render(request, 'authentication/admin/ahighlights.html', {
                'form': form,
                'highlights': photos
            })
    else:
        form = PhotoForm()

    photos = Photo.objects.all()
    return render(request, 'authentication/admin/ahighlights.html', {
        'form': form,
        'highlights': photos
    })



def gal(request):
    highlights = Photo.objects.all()
    return render(request, 'authentication/user/gal.html', {'highlights': highlights})

def view_photos(request):
    photos = Photo.objects.all()
    return render(request, 'authentication/user/gal.html', {'photos': photos})

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

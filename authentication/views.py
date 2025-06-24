from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import PhotoForm
from .models import Photo
from .forms import MediaForm
from .models import Media
from .models import Files
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



def uhighlights(request):
    highlights = Photo.objects.all()
    return render(request, 'authentication/user/uhighlights.html', {'highlights': highlights})

def view_photos(request):
    photos = Photo.objects.all()
    return render(request, 'authentication/user/uhighlights.html', {'photos': photos})

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

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/dashboard')
        else:
            # Trigger JS alert on failure
            return render(request, "authentication/signin.html", {
                'username': username,
                'login_failed': True
            })
    return render(request, "authentication/signin.html")




def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('home')


def uhome(request):
      return render(request, "authentication/user/uhome.html")

def gallery(request):
      return render(request, "authentication/user/gallery.html")


def home(request):
      return render(request, "authentication/index.html")

def about(request):
      return render(request, "authentication/user/about.html")

def uhighlightslery(request):
      return render(request, "authentication/user/uhighlightslery.html")

def contact(request):
      return render(request, "authentication/user/contact.html")


def ugallery(request):
      return render(request, "authentication/user/ugallery.html")

def dashboard(request):
    return render(request, "authentication/admin/dashboard.html")

def agallery(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        files = request.FILES.getlist('files')
        file_list = []

        for file in files:
            new_file = Files(file=file, title=title, description=description)
            new_file.save()
            file_list.append(new_file.file.url)

        # Fetch all files to show in the table
        all_files = Files.objects.all().order_by('-id')
        return render(request, "authentication/admin/agallery.html", {
            'new_urls': file_list,
            'files': all_files
        })

    # GET request — just show all files
    all_files = Files.objects.all().order_by('-id')
    return render(request, "authentication/admin/agallery.html", {
        'files': all_files
    })

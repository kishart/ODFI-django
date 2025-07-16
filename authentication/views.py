from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import PhotoForm
from .models import Photo
from .models import MediaGroup, MediaFile
from .models import Files
from django.shortcuts import get_object_or_404
from functools import wraps
from django.http import Http404
from .models import Highlight
from .forms import HighlightForm
from django.shortcuts import get_object_or_404, redirect



def highlight(request):
    highlights = Highlight.objects.all().order_by('-date')
    return render(request, 'authentication/admin/highlight.html', {'highlights': highlights})

def addhighlight(request):
    if request.method == 'POST':
        form = HighlightForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('highlight_list')  # Correct use of redirect
    else:
        form = HighlightForm()

    return render(request, 'authentication/admin/addhighlight.html', {'form': form})

def require_login_or_404(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise Http404("You must be signed in.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view




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


# def home(request):
#       return render(request, "authentication/index.html")

def home(request):
    highlights = Highlight.objects.all()
    return render(request, "authentication/index.html", {'highlights': highlights})

def about(request):
      return render(request, "authentication/user/about.html")

def uhighlightslery(request):
      return render(request, "authentication/user/uhighlightslery.html")

def contact(request):
      return render(request, "authentication/user/contact.html")


def ugallery(request):
      return render(request, "authentication/user/ugallery.html")

def dashboard(request):
    return render(request, 'authentication/dashboard.html', {
        'active_page': 'dashboard'
    })


def agallery(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        files = request.FILES.getlist('files')

        # Create one group for this upload
        group = MediaGroup.objects.create(title=title, description=description)

        # Create one MediaFile per uploaded file
        for file in files:
            MediaFile.objects.create(group=group, file=file)

        # Get all groups to show in table
        all_groups = MediaGroup.objects.prefetch_related('files').order_by('-id')
        return render(request, "authentication/admin/agallery.html", {
            'groups': all_groups
        })

    # GET request — just show all groups
    all_groups = MediaGroup.objects.prefetch_related('files').order_by('-id')
    return render(request, "authentication/admin/agallery.html", {
        'groups': all_groups
    })


@require_login_or_404
def dashboard(request):
    return render(request, "authentication/admin/dashboard.html")

@require_login_or_404
def education(request):
    return render(request, "authentication/admin/education.html")

@require_login_or_404
def adminis(request):
    return render(request, 'authentication/admin/adminis.html', {
        'active_page': 'adminis'
    })

@require_login_or_404
def jumuat(request):
    return render(request, "authentication/admin/jumuat.html")

@require_login_or_404
def food(request):
    return render(request, "authentication/admin/food.html")

@require_login_or_404
def ihya(request):
    return render(request, "authentication/admin/ihya.html")

# views.py

@require_login_or_404
def public(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        uploaded_files = request.FILES.getlist('files')

        if title and description and uploaded_files:
            group = MediaGroup.objects.create(title=title, description=description)
            for f in uploaded_files:
                MediaFile.objects.create(group=group, file=f)

            return redirect('public')  # Replace with your actual view name

    groups = MediaGroup.objects.prefetch_related('files').order_by('-uploaded_at')
    return render(request, 'authentication/admin/public.html', {'groups': groups})

@require_login_or_404
def qurban(request):
    return render(request, "authentication/admin/qurban.html")

@require_login_or_404
def services(request):
    return render(request, "authentication/admin/services.html")

@require_login_or_404
def dawah(request):
    return render(request, "authentication/admin/dawah.html")


def edit_highlight(request, pk):
    highlight = get_object_or_404(Highlight, pk=pk)
    if request.method == 'POST':
        form = HighlightForm(request.POST, request.FILES, instance=highlight)
        if form.is_valid():
            form.save()
            return redirect('highlight_list')  # change to your highlight page name
    else:
        form = HighlightForm(instance=highlight)
    return render(request, 'authentication/admin/edit_highlight.html', {'form': form})

def delete_highlight(request, pk):
    highlight = get_object_or_404(Highlight, pk=pk)
    if request.method == 'POST':
        highlight.delete()
        return redirect('highlight_list')  # change to your highlight page name
    
def custom_404_view(request, exception):
    return render(request, '404.html', status=404)






def edit_photos(request, group_id):
    group = get_object_or_404(MediaGroup, id=group_id)

    if request.method == 'POST':
        group.title = request.POST.get('title')
        group.description = request.POST.get('description')
        group.save()

        # Handle new files if uploaded
        files = request.FILES.getlist('files')
        for file in files:
            MediaFile.objects.create(group=group, file=file)

        return redirect('agallery')

    return render(request, 'authentication/admin/edit_photos.html', {'group': group})


def delete_group(request, group_id):
    group = get_object_or_404(MediaGroup, id=group_id)
    if request.method == 'POST':
        group.delete()
        return redirect('agallery')
"""
URL configuration for odfi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', include('authentication.urls')),
    # path('upload/', views.upload_photo, name='upload_photo'),
    path('gallery/', views.view_photos, name='gallery'),
    path('uhighlights/', views.uhighlights, name='uhighlights'),
    path('ahighlights/', views.upload_photos, name='ahighlights'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('adminis/', views.adminis, name='adminis'),
    path('education/', views.education, name='education'),

    path('dawah/', views.dawah, name="dawah"),
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
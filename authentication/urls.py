from django.contrib import admin
from django.urls import path, include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('', views.home, name="home"),
   path('signup', views.signup, name="signup"),
   path('signin', views.signin, name="signin"),
   path('signout', views.signout, name="signout"),
   path('uhome', views.uhome, name="uhome"),
   path('about/', views.about, name="about"),
   path('gallery/', views.gallery, name="gallery"),
   path('contact/', views.contact, name="contact"),
   path('ahighlights/', views.ahighlights, name="ahighlights"),
  
   path('gal/', views.gal, name="gal"),
   path('edit/<int:photo_id>/', views.edit_photo, name='edit_photo'),
path('delete/<int:photo_id>/', views.delete_photo, name='delete_photo'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
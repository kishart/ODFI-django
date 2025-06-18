from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
   path('', views.home, name="home"),
   path('signup', views.signup, name="signup"),
   path('signin', views.signin, name="signin"),
   path('signout', views.signout, name="signout"),
   path('uhome', views.uhome, name="uhome"),
   path('about/', views.about, name="about"),

   path('gallery/', views.gallery, name="gallery"),
    path('contact/', views.contact, name="contact"),
]
 
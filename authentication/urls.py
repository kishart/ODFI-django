from django.contrib import admin
from django.urls import path, include
from .import views
from django.conf import settings
from django.conf.urls.static import static
from .views import highlight, addhighlight


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
  
   path('uhighlights/', views.uhighlights, name="uhighlights"),
   path('edit/<int:photo_id>/', views.edit_photo, name='edit_photo'),
path('delete/<int:photo_id>/', views.delete_photo, name='delete_photo'),
path('ugallery/', views.ugallery, name="ugallery"),   
path('agallery/', views.agallery, name="agallery"),
    path('jumuat/', views.jumuat, name='jumuat'),
    path('education/', views.education, name='education'),


path('adminis/', views.adminis, name='adminis'),

 path('dashboard', views.dashboard, name="dashboard"),
 path('food/', views.food, name="food"),
 path('dawah/', views.dawah, name="dawah"),
 path('ihya/', views.ihya, name="ihya"),
 path('public/', views.public, name="public"),
 path('qurban/', views.qurban, name="qurban"),
 path('services/', views.services, name="services"),
     path('highlight/', highlight, name='highlight_list'),
       
    path('addhighlight/', addhighlight, name='add_highlight'),
      path('highlights/edit/<int:pk>/', views.edit_highlight, name='edit_highlight'),
    path('highlights/delete/<int:pk>/', views.delete_highlight, name='delete_highlight'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'authentication.views.custom_404_view'

from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
# Remove direct import if already using 'views' for all references
# If you need to use highlight, addhighlight, addgallery, addvideos directly, ensure they exist in views.py
# Otherwise, just use 'views.highlight', etc. in urlpatterns


urlpatterns = [
   path('', views.home, name="home"),
   path('signup', views.signup, name="signup"),
   path('signin', views.signin, name="signin"),
   path('signout', views.signout, name="signout"),
   path('uhome', views.uhome, name="uhome"),
   path('about/', views.about, name="about"),
   path('gallery/', views.gallery, name="gallery"),
   path('contact/', views.contact, name="contact"),
  
path('ugallery/', views.ugallery, name="ugallery"),   
path('agallery/', views.agallery, name="agallery"),

       path('gallery/edit/<int:group_id>/', views.edit_photos, name='edit_photos'),
    path('gallery/delete/<int:group_id>/', views.delete_group, name='delete_group'),


    path('avideos/', views.avideos, name="avideos"),
path('videos/edit/<int:group_id>/', views.edit_videos, name='edit_videos'),
path('videos/delete/<int:group_id>/', views.delete_videos, name='delete_videos'),

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

 path('appendices/', views.appendices, name="appendices"),
    #  path('highlight/', views.highlight, name='highlight_list'),
          path('highlight/', views.highlight, name='highlight'),
    path('addhighlight/', views.addhighlight, name='addhighlight'),

    path('addgallery/', views.addgallery, name='addgallery'),
    path('addvideos/', views.addvideos, name='addvideos'),

path('highlights/edit/<int:photo_id>/', views.edit_highlights, name='edit_highlights'),
path('highlight/delete/<int:photo_id>/', views.delete_highlights, name='delete_highlights'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'authentication.views.custom_404_view'

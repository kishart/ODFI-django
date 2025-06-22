from django import forms
from .models import Photo
from .models import Media  # Assuming you want to use the Media model as well


class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['category', 'file', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }
        
class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['type', 'title', 'description', 'date', 'image']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }


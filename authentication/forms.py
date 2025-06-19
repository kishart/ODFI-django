from django import forms

class PhotoForm(forms.Form):
    photos = forms.FileField(
        widget=forms.ClearableFileInput(),  # No `multiple=True` here
        required=True
    )

    
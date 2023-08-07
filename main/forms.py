from django import forms
from .models import GalleryModel









class GalleryModelForm(forms.ModelForm):
    

    class Meta:
        model=GalleryModel
        fields= ('name', 'image')



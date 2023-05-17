from django import forms
#from django.core import validators
from .models import Dataset


class UploadForm(forms.ModelForm):
    class Meta:
        model = Dataset
        fields = ['data_file','name']

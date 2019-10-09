from django import forms
from django.forms import fields, models, formsets, widgets
from .models import File


class FileModelForm(forms.ModelForm):
    class Meta:
        model = File
        exclude = ['hash', 'file_name']

    file = forms.FileField(label='File to upload:')
    date_to = forms.DateField(label='File will be available to date:', widget=forms.SelectDateWidget, required=False)
    password = forms.CharField(label='Set password for access protection:', widget=forms.PasswordInput, required=False)


class PasswordForm(forms.Form):
    password = forms.CharField(label='Set password for access:', widget=forms.PasswordInput, required=True)
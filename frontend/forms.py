from django import forms
from django.contrib.auth.models import User
from .models import Link

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)

    class Meta:
        fields = ['username', 'password']

class LinkForm(forms.ModelForm):

    class Meta:
        model = Link
        fields = ['title', 'url']
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from .models import *

class RegisterUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    phone_number = forms.CharField( widget=forms.TextInput(attrs={'type':'number'}))


    class Meta:
        model = User
        fields = ['username','email','phone_number']

    # validate password

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password2'] != cd['password']:
            raise ValidationError('Password dont match !!!')

        return cd['password2']

class AdminUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['username','email']

    # validate password

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password2'] != cd['password']:
            raise ValidationError('Password dont match !!!')

        return cd['password2']
from django.contrib.auth.models import User
from django import forms
from .models import *

class RegisterUserForm(forms.ModelForm):
    email=forms.EmailField(max_length=50)
    username=forms.CharField(max_length=10)
    mobile_no = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
            model = UserProfile
            fields =['username', 'email', 'mobile_no','password']


class LoginUserForm(forms.Form):
        email = forms.EmailField(max_length=50)
        password = forms.CharField(widget=forms.PasswordInput)
        def __init__(self, *args, **kwargs):
        	super(LoginUserForm, self).__init__(*args, **kwargs)
        	for field in self.fields.values():
         		field.widget.attrs = {'class': 'form-control'}


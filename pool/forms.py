from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model



class RegisterUserForm(forms.ModelForm):
    email=forms.EmailField(max_length=50)
    name=forms.CharField(max_length=10)
    mobile_no = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
    	    field.widget.attrs = {'class': 'form-control'}

    class Meta:
            model = UserProfile
            fields =['email', 'name', 'mobile_no', 'password']


class LoginUserForm(forms.Form):
        email = forms.EmailField(max_length=50)
        password = forms.CharField(widget=forms.PasswordInput)
        def __init__(self, *args, **kwargs):
            super(LoginUserForm, self).__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs = {'class': 'form-control'}

class CommentForm(forms.ModelForm):
        model = Comment
        fields = ('comment')

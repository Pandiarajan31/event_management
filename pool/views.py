from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import FormView
from django.http import HttpResponseForbidden
from django.http import HttpResponse,HttpResponseRedirect
from .forms import *
from django.http import *
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import *
from django.db import models
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from  django.views import  generic
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.

class RegistrationView(CreateView):

        template_name = "register.html"
        form_class = RegisterUserForm
        success_url = '/account/login/'


class LoginView(FormView):
        template_name = "registration/login.html"
        form_class = LoginUserForm
        success_url = '/account/home'

        def form_valid(self, form):
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(email=email, password=password)
            if user is not None:
                if user.is_active:
                    login(self.request, user)
            return super(LoginView, self).form_valid(form)

class HomeView(LoginRequiredMixin, generic.ListView):
        template_name = "home.html"
        model = Item

        def get_context_data(self, **kwargs):
            context = super(HomeView, self).get_context_data(**kwargs)
            print(context)
            return context



class AdPostingView(CreateView):
        template_name = "event/postevent.html"
        model = Item
        success_url = '/view/'
        fields = '__all__'

class view(LoginRequiredMixin, ListView):
        paginate_by = 10
        model = Item
        template_name = "view.html"

class ItemDetail(LoginRequiredMixin, DetailView):
        model = Item
        template_name="details.html" 

class AddComment(LoginRequiredMixin, CreateView):
        template_name = "details.html"
        model = Comment
        fields = '__all__'

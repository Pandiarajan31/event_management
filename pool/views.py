from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import FormView
from django.http import HttpResponseForbidden
from django.http import HttpResponse,HttpResponseRedirect
from .forms import *
from django.contrib.auth.models import User
from django.db import models
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .decorators import staff_required
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


# Create your views here.

class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = "register.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseForbidden()

        return super(RegisterUserView, self).dispatch(request, *args, **kwargs)

    def form_valid(self,form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return HttpResponse('User Registered')

class AdminUserView(CreateView):
    form_class = AdminUserForm
    template_name = "reg.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseForbidden()

        return super(AdminUserView, self).dispatch(request, *args, **kwargs)

    def form_valid(self,form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return HttpResponse('User Registered')

class AdPostingView(CreateView):
        # pass
        template_name = "realapp/postevent.html"
        model = Item
        success_url = '/thanks/'
        fields = '__all__'

class view(ListView):
        paginate_by = 10
        model = Item
        template_name = "view.html"

class ItemDetail(DetailView):
        model = Item
        template_name="details.html" 
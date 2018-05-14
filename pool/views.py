from django.conf import settings
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
from braces.views import SuperuserRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.core.signing import Signer






# Create your views here.

class RegisterUserView(FormView):

        template_name = "register.html"
        form_class = RegisterUserForm
        success_url = '/account/login'

        def form_valid(self, form):
            if form.is_valid():
                save_it = form.save(commit = False)
                UserProfile.objects.create_user(form.cleaned_data.get('email'),
                                                  form.cleaned_data.get('password'),
                                                  form.cleaned_data.get('mobile_no'),
                                                  form.cleaned_data.get('name')                                     
                                                  )
            
                subject = "Thanku"
                message = "Welcome"
                from_email = settings.EMAIL_HOST_USER
                to_list = [save_it.email]

                send_mail(subject,message,from_email,to_list)

            return super().form_valid(form)



class LoginUserView(FormView):

        template_name = "registration/login.html"
        form_class = LoginUserForm

        def post(self, request, *args, **kwargs):
                email = request.POST['email']
                password = request.POST['password']

                user = authenticate(request, email=email, password=password)
                print("auth", str(authenticate(email=email, password=password)))

                if user is not None:
                        login(request, user)
                        return HttpResponseRedirect('/view/')

                else:
                        return HttpResponse("wrong input")

class HomeView(generic.ListView):
        template_name = "home.html"
        paginate_by = 10
        model = Item

class AdPostingView(SuperuserRequiredMixin, CreateView):
        template_name = "event/postevent.html"
        model = Item
        success_url = '/view/'
        fields = '__all__'

class view(LoginRequiredMixin, ListView):
        paginate_by = 10
        model = Item
        template_name = "view.html"

class ItemDetail(LoginRequiredMixin, DetailView):
        model =  Item
        template_name="details.html" 
        
        if request.method == 'POST':
            comment_form= CommentForm(request.POST or None)
            if comment_form_is_valid():
                
             else:
                 comment_form = CommentForm()


        def get_context_data(self,  **kwargs):
            context = super(ItemDetail, self).get_context_data(**kwargs)
            context['comment'] = Comment.objects.all().order_by('id')
            return context
         

class UpdateEvent(SuccessMessageMixin, UpdateView):
        template_name = "event/postevent.html"
        model = Item
        success_url = reverse_lazy("eventposting")
        success_message = "Updated successfully"
        fields = '__all__'

class DeleteEvent(SuccessMessageMixin, DeleteView):
        model = Item
        success_url = reverse_lazy('display')
        template_name = "view.html"
        success_message = "Deleted successfully"
        fields = '__all__'


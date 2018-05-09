from django.urls import path
from django.contrib.auth.views import LogoutView
from django.conf.urls import url,include
from django.views.generic import TemplateView
from . import views
from .views import LoginView,RegistrationView,HomeView,AdPostingView,view,ItemDetail,AddComment


urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name="register"),
    path('home/', views.HomeView.as_view(), name="home"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/',LogoutView.as_view(), name="logout"),
    path('eventposting/',views.AdPostingView.as_view(),name="eventposting")
]
# urlpatterns = [
#     url(r'^register/', include('accounts.urls')), # add .urls after app name
# ]

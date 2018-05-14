from django.urls import path
from django.contrib.auth.views import LogoutView
from django.conf.urls import url,include
from django.views.generic import TemplateView
from . import views
from .views import LoginUserView,RegisterUserView,AdPostingView,view,ItemDetail





urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name="register"),
    path('login/', views.LoginUserView.as_view(), name="login"),
    path('logout/',LogoutView.as_view(), name="logout"),
    path('eventposting/',views.AdPostingView.as_view(),name="eventposting"),
    path('edit/<pk>/',views.UpdateEvent.as_view(),name="eventupdate"),
    path('delete/<pk>/',views.DeleteEvent.as_view(),name="eventdelete")
]
# urlpatterns = [
#     url(r'^register/', include('accounts.urls')), # add .urls after app name
# ]

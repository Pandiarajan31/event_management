from django.conf.urls import url,include
from .views import RegisterUserView
from .views import AdminUserView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^register/$', view=RegisterUserView.as_view(),name='register'),
    url(r'^adminregister/$', view=AdminUserView.as_view(),name='adminregister'),
    url(r'^login/$', auth_views.login,name='login'),
    url(r'^logout/$', auth_views.logout,name='logout'),
    url(r'^eventposting/$',views.AdPostingView.as_view(),name="adposting")
]
# urlpatterns = [
#     url(r'^register/', include('accounts.urls')), # add .urls after app name
# ]

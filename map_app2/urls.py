from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView 


urlpatterns = [
    path('home', views.home, name='home'),  # This sets the homepage to the home() view
]

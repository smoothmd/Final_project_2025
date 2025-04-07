from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView 


urlpatterns = [
    path('', views.home, name='home'),  # This sets the homepage to the home() view
    path('login/', views.login, name='login'),  # Login page
    path('profile', views.profile, name='profile'),  # User profile
    path('signnup', views.signup, name='signup'),
    #path('logout/', LogoutView.as_view(next_page='login'), name='logout'),  # Log out
]

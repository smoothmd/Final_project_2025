from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView 


urlpatterns = [
    path('', views.home, name='home'),  # This sets the homepage to the home() view
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    #path('logout/', LogoutView.as_view(next_page='login'), name='logout'),  # Log out
]

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
#from .forms import SignUpForm, UserProfileForm
#from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    #return HttpResponse("Hello world!")
    return render(request, 'index.html')  # Make sure this is the correct file

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'map_app2/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'map_app2/login.html', {'error': 'Invalid credentials'})
    return render(request, 'map_app2/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile_view(request):
    try:
        # Retrieve user data
        user = request.user
        if not user.is_authenticated:
            raise ValueError("User is not logged in.")

        # Pass user data to the profile page
        return render(request, 'map_app2/profile.html', {'user': user})

    except ValueError as e:
        # Handle case where user is not logged in
        messages.error(request, str(e))

        return redirect('map_app2/login.html')  # Redirect to login page
#return HttpResponse('ValueError exception: '+ str(e))
    except Exception as e:
        # Handle unexpected errors
        messages.error(request, 'An error occurred' + str(e))

        return redirect('map_app2/login.html')  # Redirect to login page
#return HttpResponse('unexpected errors exception: '+ str(e))
# Signup page view
    #return render(request, 'map_app2/profile.html', {'user': request.user})

def home(request):
    #return HttpResponse("Hello world!")
    return render(request, 'index.html')  # Make sure this is the correct file
#def profile(request):
    #return render(request, 'profile.html')


# def logout_view(request):
#     logout(request)
#     return redirect("login")

# 
# def login(request): 
#     return render(request, 'login.html') 

#def signup(request): 
    #return render(request, 'signup.html') 

#

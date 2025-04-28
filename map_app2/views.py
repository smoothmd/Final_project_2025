from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import json
from django.http import JsonResponse

from .models import SavedLocation 
from django.views.decorators.csrf import csrf_exempt
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
        if not username or not password:
            messages.error(request, 'Both username and password are required.')
            return render(request, 'login.html')

        if user:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'map_app2/login.html', {'error': 'Invalid credentials'})
    return render(request, 'map_app2/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

from django.shortcuts import render
from .models import SavedLocation

def dashboard(request):
    user_saved_locations = SavedLocation.objects.filter(user=request.user)
    saved_locations = [
        {
            'location': loc.city,        # Rename field for JS
            'lat': loc.latitude,          # Rename field for JS
            'lon': loc.longitude,         # Rename field for JS
            'temperature': loc.temperature,
            'wind_speed': loc.wind_speed,
            'description': loc.description,
        }
        for loc in user_saved_locations
    ]

    return render(request, 'dashboard.html', {
        'saved_locations': saved_locations,
    })


@login_required
def profile_view(request):
    try:
        user_saved_locations = SavedLocation.objects.filter(user=request.user)
        saved_locations = [
            {
                'location': loc.city,
                'lat': loc.latitude,
                'lon': loc.longitude,
                'temperature': loc.temperature,
                'wind_speed': loc.wind_speed,
                'description': loc.description,
            }
            for loc in user_saved_locations
        ]
    except Exception as e:
        messages.error(request, f"Error loading saved locations: {e}")
        saved_locations = []

    context = {
        'user': request.user,
        'saved_locations': saved_locations,
    }
    return render(request, 'map_app2/profile.html', context)

#return HttpResponse('unexpected errors exception: '+ str(e))
# Signup page view
    #return render(request, 'map_app2/profile.html', {'user': request.user})

def home(request):
   
    return render(request, 'index.html')  # Make sure this is the correct file
#def profile(request):
    #return render(request, 'profile.html')

@csrf_exempt
@login_required
def save_point(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print("Incoming JSON:", data)

            # Correct mapping
            latitude = data.get("lat")
            longitude = data.get("lon")
            city = data.get("location")
            temperature = data.get("temperature")
            wind_speed = data.get("wind_speed")  
            description = data.get("description")  # ✅ get description too

            if not all([city, latitude, longitude]):
                return JsonResponse({"status": "fail", "error": "Missing required fields"}, status=400)

            SavedLocation.objects.create(
                user=request.user,
                city=city,
                latitude=latitude,
                longitude=longitude,
                temperature=temperature,
                wind_speed=wind_speed,
                description=description
            )

            return JsonResponse({"status": "success"})

        except json.JSONDecodeError:
            return JsonResponse({"status": "fail", "error": "Invalid JSON"}, status=400)
        except Exception as e:
            print("Unexpected error:", str(e))
            return JsonResponse({"status": "fail", "error": str(e)}, status=500)

    return JsonResponse({"status": "fail", "error": "Invalid method"}, status=400)


# def logout_view(request):
#     logout(request)
#     return redirect("login")

# 
# def login(request): 
#     return render(request, 'login.html') 

#def signup(request): 
    #return render(request, 'signup.html') 

#

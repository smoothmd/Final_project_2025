from django.db import models
from django.contrib.auth.models import User

class SavedLocation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField(null=True, blank=True) 
    wind_speed = models.FloatField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
      return f"{self.city} ({self.latitude}, {self.longitude})"  
#return f"{self.city} ({self.user.username})"

# Create your models here.

from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('', include('staff.urls')),
    path('tyres', include('tyres.urls')),
    path('parking',include ('parking.urls')),
]
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('', include('staff.urls')),
    path('tyre/', include('tyres.urls')),
    path('parking',include ('parking.urls')),
]
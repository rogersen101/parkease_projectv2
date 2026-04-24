from django.urls import path
from . import views

urlpatterns = [
    path('', views.tyre_service, name='tyre_service'),
    path('battery/', views.battery, name='battery'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('tyre_service', views.tyre_service, name='tyre_service')
]
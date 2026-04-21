from django.contrib import admin
from django.urls import path
from parking import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard', views.dashboard, name='dashboard'),
    path('', views.register, name='register'),
    path('list/', views.vehicle_list, name='vehicle_list'),
  ]

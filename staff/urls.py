from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('staff_register/', views.staff_register, name='staff_register'),
    path('logout/', views.logout_view, name='logout'),
]
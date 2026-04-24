from django.shortcuts import render, redirect
from .forms import TyreForm,BatteryForm
from .models import TyreService

# Create your views here.

def tyre_service(request):
    form = TyreForm(request.POST or None)
    if request.method == 'POST' and form.is_valid(): # Added method check for safety
        form.save()
        return redirect('dashboard')
    return render(request, 'tyre.html', {'form': form})

def battery(request):
    form = BatteryForm(request.POST or None)
    # Added parentheses () to is_valid
    if request.method == 'POST' and form.is_valid(): 
        form.save()
        return redirect('dashboard')
    return render(request, 'battery.html', {'form': form})
    
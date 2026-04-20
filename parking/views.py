from django.shortcuts import render,redirect
from .models import Vehicle
from .forms import VehicleForm

# Create your views here.
def parking(request):

    return render(request,'parking.html')

def register(request):
    form = VehicleForm()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        


    return render(request, 'register.html', {'form': form})
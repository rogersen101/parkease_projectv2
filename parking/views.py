from django.shortcuts import render,redirect
from .models import Vehicle
from .forms import VehicleForm

# Create your views here.
# # def dashboard(request):
#     search = request.GET.get('search')

#     vehicles = Vehicle.objects.all()

#     if search:
#         vehicles = vehicles.filter(number_plate__icontains=search)

#     context = {
#         'vehicles': vehicles,
#         'revenue': 0  
#     }

#     return render(request, 'dashboard.html', context)

def dashboard(request):

    return render(request,'dashboard.html')

def register(request):
    form = VehicleForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')

    return render(request, 'register.html', {'form': form})

def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicle_list.html',{'vehicles':vehicles})

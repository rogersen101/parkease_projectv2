from django.shortcuts import render,redirect,get_object_or_404
from .models import Vehicle,SignOut
from .forms import VehicleForm,SignOutForm
from .models import Payment
from parking.utils import calculate_parking_fee
# from payments.models import Payment

# Create your views here.
def dashboard(request):
    search = request.GET.get('search')

    vehicles = Vehicle.objects.all()

    if search:
        vehicles = vehicles.filter(number_plate__icontains=search)

    context = {
        'vehicles': vehicles,
        'revenue': 0  
    }

    return render(request, 'dashboard.html', context)

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

def generate_receipt(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)

    amount = calculate_parking_fee(vehicle)

    payment = Payment.objects.create(
        vehicle=vehicle,
        amount=amount
    )

    return render(request, 'receipt.html', {
        'payment': payment
    })

def signout_vehicle(request, vehicle_id):
    vehicle = Vehicle.objects.get(id=vehicle_id)

    form = SignOutForm(request.POST or None)

    if form.is_valid():
        receipt_number = form.cleaned_data['receipt_number']

        # 🔥 Validate receipt exists
        if not Payment.objects.filter(receipt_number=receipt_number).exists():
            form.add_error('receipt_number', 'Invalid receipt number')
        else:
            signout = form.save(commit=False)
            signout.vehicle = vehicle
            signout.save()

            # update vehicle status
            vehicle.status = 'cleared'
            vehicle.save()

            return redirect('vehicle_list')

    return render(request, 'signout.html', {
        'form': form,
        'vehicle': vehicle
    })



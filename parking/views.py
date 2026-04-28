from django.shortcuts import render,redirect,get_object_or_404
from .models import Vehicle,SignOut
from .forms import VehicleForm,SignOutForm
from .models import Payment
from tyres.models import Battery,TyreService
from parking.utils import calculate_parking_fee
from django.db.models import Sum
from django.utils import timezone
# from payments.models import Payment

# Create your views here.


def dashboard(request):
    search = request.GET.get('search')

    vehicles = Vehicle.objects.all()

    if search:
        vehicles = vehicles.filter(number_plate__icontains=search)

    # Today's revenue
    today = timezone.now().date()
    today_revenue = Payment.objects.filter(
        created_at__date=today
    ).aggregate(total=Sum('amount'))['total'] or 0

    # total slots 
    total_slots = 150
    occupied = Vehicle.objects.filter(status='parked').count()
    available_slots = total_slots - occupied

    return render(request, 'dashboard.html', {
        'vehicles': vehicles,
        'today_revenue': today_revenue,
        'available_slots': available_slots
    })

def register(request):
    form = VehicleForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard')

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

def admin_dashboard(request):
    date = request.GET.get('date')

    payments = Payment.objects.all()
    tyres = TyreService.objects.all()
    batteries = Battery.objects.all()
    signouts = SignOut.objects.all()

    if date:
        payments = payments.filter(created_at__date=date)
        tyres = tyres.filter(created_at__date=date)
        batteries = batteries.filter(created_at__date=date)
        signouts = signouts.filter(signout_time__date=date)

    parking_revenue = payments.aggregate(total=Sum('amount'))['total'] or 0
    tyre_revenue = tyres.aggregate(total=Sum('amount'))['total'] or 0
    battery_revenue = batteries.aggregate(total=Sum('price'))['total'] or 0

    total_revenue = parking_revenue + tyre_revenue + battery_revenue

    return render(request, 'admin_dashboard.html', {
        'parking_revenue': parking_revenue,
        'tyre_revenue': tyre_revenue,
        'battery_revenue': battery_revenue,
        'total_revenue': total_revenue,
        'signouts': signouts
    })
#edit vehicle view
def edit_vehicle(request, id):
    vehicle = get_object_or_404(Vehicle, id=id)

    form = VehicleForm(request.POST or None, instance=vehicle)

    if form.is_valid():
        form.save()
        return redirect('vehicle_list')

    return render(request, 'edit_vehicle.html', {
        'form': form
    })

def delete_vehicle(request, id):
    vehicle = get_object_or_404(Vehicle, id=id)

    if request.method == 'POST':
        vehicle.delete()
        return redirect('vehicle_list')

    return render(request, 'delete_vehicle.html', {
        'vehicle': vehicle
    })



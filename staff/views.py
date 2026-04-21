from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Staff
from .forms import StaffForm, StaffLoginForm
from django.contrib.auth import login as log,logout

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = StaffLoginForm(request, data = request.POST)

        if form.is_valid():
            user = form.get_user()
            log(request, user)
            return redirect('dashboard')
    else:
        form = StaffLoginForm()

    return render(request,'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StaffForm()
    return render(request,'register.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')





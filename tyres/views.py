from django.shortcuts import render, redirect
from .forms import TyreForm
from .models import TyreService

# Create your views here.

def tyre_service(request):
    form = TyreForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request,'tyre.html',{'form':form})
    
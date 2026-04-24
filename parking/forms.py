from django import forms
from .models import Vehicle,SignOut


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'

class SignOutForm(forms.ModelForm):
    class Meta:
        model = SignOut
        fields = '__all__'


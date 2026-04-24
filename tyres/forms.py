from django import forms
from .models import TyreService, Battery
from parking.models import Vehicle

class TyreForm(forms.ModelForm):

    class Meta:
        model = TyreService
        fields = ['vehicle', 'service_type', 'amount']

        widgets = {
            'vehicle': forms.Select(attrs={'class': 'form-control'}),
            'service_type': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    # 🔒 Validation: amount must be positive
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')

        if amount <= 0:
            raise forms.ValidationError("Amount must be greater than zero")

        return amount
class BatteryForm(forms.ModelForm):

    class Meta:
        model = Battery
        fields = ['vehicle', 'type', 'price']

        widgets = {
            'vehicle': forms.Select(attrs={'class': 'form-control'}),
            'type': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    # 🔒 Validation: price must be positive
    def clean_price(self):
        price = self.cleaned_data.get('price')

        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero")

        return price
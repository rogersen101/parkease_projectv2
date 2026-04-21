from django import forms
from .models import TyreService
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
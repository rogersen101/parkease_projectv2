from django import forms
from .models import Vehicle, SignOut
import re


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
        error_messages = {
            'driver_name' :{'required':'please enter driver name'},
            'vehicle_type' :{'required':'please enter vehicle type'},
            'number_plate' :{'required':'please enter plate'},
            'model_color' :{'required':'please model_color'},
            'phone' :{'required':'please enter phone number'},
            'nin' :{'required':'please enter nin'},
            'status' :{'required':'please enter status'}
        }
    # Driver name validation
    def clean_driver_name(self):
        name = self.cleaned_data.get('driver_name')

        if not name.isalpha():
            raise forms.ValidationError("Name must contain only letters")

        if not name[0].isupper():
            raise forms.ValidationError("Name must start with a capital letter")

        if len(name) < 2:
            raise forms.ValidationError("Name must be at least 2 characters")

        return name
    # vehicle plate validation
    def clean_number_plate(self):
        plate = self.cleaned_data.get('number_plate').upper()

        if not plate.startswith('U'):
            raise forms.ValidationError("Number plate must start with 'U'")

        if not re.match(r'^U[A-Z0-9]{5,6}$', plate):
            raise forms.ValidationError("Enter a valid Ugandan plate (e.g UBA123)")

        return plate

    # Phone Number Validation
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if not re.match(r'^07\d{8}$', phone):
            raise forms.ValidationError("Enter a valid Ugandan number (e.g 0700000000)")

        return phone

    #  NIN VALIDATION (ONLY FOR BODA)
    def clean(self):
        cleaned_data = super().clean()

        vehicle_type = cleaned_data.get('vehicle_type')
        nin = cleaned_data.get('nin')

        if vehicle_type == 'boda' and not nin:
            raise forms.ValidationError("NIN is required for boda-boda")

        return cleaned_data



class SignOutForm(forms.ModelForm):


    GENDER_CHOICES = [
        ('', 'Select Gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = SignOut
        fields = '__all__'

        widgets = {
            'receiver_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter receiver name'
            }),
            'receipt_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter receipt number'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g 0700000000'
            }),
            'nin': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter NIN'
            }),
        }

        labels = {
            'receiver_name': 'Receiver Name',
            'receipt_number': 'Receipt Number',
            'phone': 'Phone Number',
            'gender': 'Gender',
            'nin': 'NIN',
        }

        error_messages = {
            'receiver_name': {
                'required': 'Please enter receiver name'
            },
            'receipt_number': {
                'required': 'Receipt number is required'
            },
            'phone': {
                'required': 'Phone number is required'
            },
            'nin': {
                'required': 'NIN is required'
            }
        }

   
    

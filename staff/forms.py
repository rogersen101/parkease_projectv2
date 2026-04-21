from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Staff

class StaffForm(UserCreationForm):
    class Meta:
        model = Staff
        fields = ['username', 'email', 'role', 'first_name','last_name','password1', 'password2']

class StaffLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs = {
            'placeholder': 'Enter username'
        }),
        error_messages = {
             'required':'please enter username'
         }
    )
    password = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                'placeholder': 'Please enter your password'
            }
        ),
        error_messages= {
            'required': 'please enter your password!'
        }
    )

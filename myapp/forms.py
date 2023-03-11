from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import*

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget = forms.EmailInput(attrs = {'class': 'form-control'}))

    class Meta():
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs = {'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class ContactForm(forms.ModelForm):
    class Meta():
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['content'].widget.attrs['class'] = 'form-control'

class BookingForm(forms.ModelForm):
    class Meta():
        model = Booking
        fields = ['choices', 'phoneNumber', 'transport', 'accomodation']
        widgets = {
            'username': forms.TextInput(attrs = {'style': 'border-radius: 1rem'}),
            'email': forms.TextInput(attrs = {'style': 'border-radius: 1rem'}),
            'phoneNumber': forms.TextInput(attrs = {'style': 'border-radius: 1rem'}),
        }

class AnonymousBookingForm(forms.ModelForm):
    class Meta():
        model = Booking
        fields = ['choices', 'username', 'email', 'phoneNumber', 'transport', 'accomodation']
        widgets = {
            'username': forms.TextInput(attrs = {'style': 'border-radius: 1rem'}),
            'email': forms.TextInput(attrs = {'style': 'border-radius: 1rem'}),
            'phoneNumber': forms.TextInput(attrs = {'style': 'border-radius: 1rem'}),
        }
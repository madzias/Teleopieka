from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *

class DodajZgloszenie(ModelForm):
    class Meta:
        model = Zgloszenie
        fields = ['status', 'rodzaj', 'pacjent', 'opis']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'rodzaj': forms.Select(attrs={'class': 'form-control'}),
            'pacjent': forms.Select(attrs={'class': 'form-control'}),
            'opis': forms.Textarea(attrs={'class': 'form-control'}),
        }

class DodajPacjenta(ModelForm):
    class Meta:
        model = Pacjent
        fields = ['status', 'nr_IMEI', 'imie_i_nazwisko']
        widgets = {
            'status':forms.Select(attrs={'class': 'form-control'}),
            'nr_IMEI': forms.TextInput(attrs={'class': 'form-control'}),
            'imie_i_nazwisko':forms.TextInput(attrs={'class': 'form-control'}),
        }

class DodajAsystenta(ModelForm):
    class Meta:
        model = Asystent
        fields = ['imie_i_nazwisko', 'telefon', 'email']

        widgets = {
            'imie_i_nazwisko':forms.TextInput(attrs={'class': 'form-control'}),
            'telefon':forms.TextInput(attrs={'class': 'form-control'}),
            'email':forms.TextInput(attrs={'class': 'form-control'})
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
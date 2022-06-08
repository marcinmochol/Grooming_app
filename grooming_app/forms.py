from django.forms import ModelForm
from django import forms
from grooming_app.models import Dogs, Clients, Employees, Service, Reservation


class DogsForm(ModelForm):
    class Meta:
        model = Dogs
        exclude = ['clients']

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ['service_name', 'price']

class LoginForm(forms.Form):
    login = forms.CharField(label='Login')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class ClientForm(ModelForm):
    class Meta:
        model = Clients
        fields = '__all__'

class EmployeeForm(ModelForm):
    class Meta:
        model = Employees
        exclude = ['dog']

from django.forms import ModelForm
from django import forms
from grooming_app.models import Dogs, Clients, Employees, Service, Reservation
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget

Hours = (
    ('8:00', '8:00'),
    ('9:00', '9:00'),
    ('10:00', '10:00'),
    ('11:00', '11:00'),
    ('12:00', '12:00'),
    ('13:00', '13:00'),
    ('14:00', '14:00'),
    ('15:00', '15:00'),
    ('16:00', '16:00'),
    ('17:00', '17:00'),
    ('18:00', '18:00'),
)

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


class ReservationForm(forms.Form):
    employye = forms.ModelChoiceField(queryset=Employees.objects)
    dog = forms.ModelChoiceField(queryset=Dogs.objects)
    service = forms.ModelChoiceField(queryset=Service.objects)
    start_day = forms.DateField(label="Start", widget=AdminDateWidget)
    start_hour = forms.TimeField(label="Start", widget=AdminTimeWidget)


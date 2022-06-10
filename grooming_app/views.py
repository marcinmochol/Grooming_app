from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import DogsForm, ServiceForm, LoginForm, EmployeeForm, ClientForm, ReservationForm
from .models import Dogs, Service, Employees, Clients
from django.views.generic import ListView

class Base(View):
    def get(self, request):
        return render(request, 'base.html')

class AddDog(View):
    def get(self, request):
        form = DogsForm()
        return render(request, 'Add_dog.html', {'form': form})

    def post(self, request):
        form = DogsForm(request.POST)
        if form.is_valid():
            dog_name = form.cleaned_data['dog_name']
            breed = form.cleaned_data['breed']
            age = form.cleaned_data['age']
            comment = form.cleaned_data['comment']
            dog = Dogs.objects.create(dog_name=dog_name, breed=breed, age=age, comment=comment)
            return HttpResponseRedirect('/dog_list')
        return render(request, 'Add_dog.html', {'form': form})

class DogsListView(ListView):
    model = Dogs
    template_name = 'dog_list.html'
    context_object_name = 'dog_list'

class ModifyDogs(View):
    def get(self, request, dog_id):
        dog = Dogs.objects.filter(id=dog_id)
        return render(request, 'Modify_dog.html', {'dog':dog})
    def post(self, request, dog_id):
        dog_name = request.POST.get('dog_name')
        breed = request.POST.get('breed')
        age = request.POST.get('age')
        comment = request.POST.get('comment')
        d = Dogs.objects.get(id=dog_id)
        d.dog_name = dog_name
        d.breed = breed
        d.age = age
        d.comment = comment
        d.save()
        return redirect("dog_list")

class DeleteDogsView(View):
    def get(self, request, dog_id):
        dog = Dogs.objects.get(id=dog_id)
        dog.delete()
        return redirect("dog_list")

class AddClient(View):
    def get(self, request):
        form = ClientForm()
        return render(request, 'Add_client.html', {'form': form})

    def post(self, request):
        form = ClientForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            e_mail = form.cleaned_data['e_mail']
            phone_number = form.cleaned_data['phone_number']
            client = Clients.objects.create(name=name, surname=surname, e_mail=e_mail, phone_number=phone_number)
            return HttpResponseRedirect('/')
        return render(request, 'Add_client.html', {'form': form})

class AddService(View):
    def get(self, request):
        form = ServiceForm()
        return render(request, 'Add_service.html', {'form': form})

    def post(self, request):
        form = ServiceForm(request.POST)
        if form.is_valid():
            service_name = form.cleaned_data['service_name']
            price = form.cleaned_data['price']
            service = Service.objects.create(service_name=service_name, price=price)
            return HttpResponseRedirect('/')
        return render(request, 'Add_service.html', {'form': form})

class AddEmployee(View):
    def get(self, request):
        form = EmployeeForm()
        return render(request, 'Add_employee.html', {'form': form})

    def post(self, request):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            e_mail = form.cleaned_data['e_mail']
            employee = Employees.objects.create(name=name, surname=surname, e_mail=e_mail)
            return HttpResponseRedirect('/')
        return render(request, 'Add_employee.html', {'form': form})

class EmployeesListView(ListView):
    model = Employees
    template_name = 'employees_list.html'
    context_object_name = 'employees_list'

class Reservation(View):
    def get(self, request):
        form = ReservationForm()
        return render(request, 'reservation.html', {'form': form})

    def post(self, request):
        form = ReservationForm(request.POST)
        if form.is_valid():
            start_day = form.cleaned_data['start_day']
            start_hour = form.cleaned_data['start_hour']
            reservation = Employees.objects.create(start_day=start_day, start_hour=start_hour)
            return HttpResponseRedirect('/')
        return render(request, 'reservation.html', {'form': form})

class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['login'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse('Wrong login or passsword')
        return render(request, 'login.html', {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')

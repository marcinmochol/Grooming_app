from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import DogsForm, ServiceForm, LoginForm
from .models import Dogs, Service
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

class AddService(View):
    def get(self, request):
        form = ServiceForm()
        return render(request, 'Add_service.html', {'form': form})

    def post(self, request, service_id):
        form = ServiceForm(request.POST)
        service_id = Service.objects.get(id=service_id)
        if form.is_valid():
            service_name = form.cleaned_data['service_name']
            price = form.cleaned_data['price']
            service = Service.objects.create(service_name=service_name, price=price)
            return HttpResponseRedirect('/')
        return render(request, 'Add_service.html', {'form': form}, {'service_id': service_id})

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
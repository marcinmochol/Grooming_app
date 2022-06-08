"""grooming_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from grooming_app.views import AddDog, AddService, LoginView, LogoutView, Base, DogsListView, AddClient, AddEmployee
from grooming_app.views import DeleteDogsView, ModifyDogs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Base.as_view()),
    path('add_dog/', AddDog.as_view(), name="add_dog"),
    path('dog_list/<int:dog_id>/', DeleteDogsView.as_view(), name="delete-dog"),
    path('dog/modify/<int:dog_id>/', ModifyDogs.as_view(), name="modify-dog"),
    path('add_service/', AddService.as_view(), name="add_service"),
    path('dog_list/', DogsListView.as_view(), name="dog_list"),
    path('add_client/', AddClient.as_view(), name="add_client"),
    path('add_employee/', AddEmployee.as_view(), name="add_employee"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]

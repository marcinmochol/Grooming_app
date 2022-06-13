from django.db import models


class Clients(models.Model):
    name = models.CharField(max_length=64, verbose_name='Imię')
    surname = models.CharField(max_length=64, verbose_name='Nazwisko')
    e_mail = models.EmailField(unique=True, verbose_name='E-mail')
    phone_number = models.CharField(max_length=9, unique=True, null=True, verbose_name='Numer telefonu')

    @property
    def full_name(self):
        return "{} {}".format(self.name, self.surname)


class Dogs(models.Model):
    dog_name = models.CharField(max_length=64, verbose_name='Imię')
    breed = models.CharField(max_length=128, null=True, verbose_name='Rasa')
    age = models.FloatField(verbose_name='Wiek')
    comment = models.TextField(null=True, verbose_name='Komentarz')
    clients = models.ManyToManyField(Clients)

    def __str__(self):
        return self.dog_name


class Employees(models.Model):
    name = models.CharField(max_length=64, verbose_name='Imię')
    surname = models.CharField(max_length=64, verbose_name='Nazwisko')
    e_mail = models.EmailField(null=True, unique=True)
    description = models.TextField(null=True, verbose_name='Opis')
    dog = models.OneToOneField(Dogs, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name



class MyReservation(models.Model):
    service = models.ForeignKey('Service', on_delete=models.CASCADE, null=True)
    dog = models.ForeignKey('Dogs', on_delete=models.CASCADE, null=True)
    start_day = models.DateField(null=True)
    start_hour = models.TimeField(null=True)
    description = models.TextField(null=True, verbose_name='Opis')


class Service(models.Model):
    service_name = models.CharField(max_length=64, verbose_name='Nazwa usługi')
    price = models.FloatField(verbose_name='Cena', null=True)

    def __str__(self):
        return self.service_name
from django.db import models

Breeds = (
    (1, "Wielorasowiec"),
    (2, "Airedale terrier"),
    (3, "Akita amerykańska"),
    (4, "Alaskan malamute"),
    (5, "York"),
    (6, "Maltańczyk"),
    (7, "Maltipoo"),
    (8, "Owczarek niemiecki"),
    (9, "West"),
    (10, "Cawapoo"),
    (11, "Cavalier"),
    (12, "Cocker spaniel"),
)

Services = (
    (1, "Kąpiele pielęgnacyjne i lecznicze"),
    (2, "Obcinanie pazurów"),
    (3, "Trymowanie"),
    (4, "Rozczesywanie"),
    (5, "Higiena uszu i zębów"),
)


class Clients(models.Model):
    name = models.CharField(max_length=64, verbose_name='Imię')
    surname = models.CharField(max_length=64, verbose_name='Nazwisko')
    e_mail = models.EmailField()
    phone_number = models.IntegerField()

    @property
    def full_name(self):
        return "{} {}".format(self.name, self.surname)


class Dogs(models.Model):
    name = models.CharField(max_length=64)
    age = models.IntegerField()
    breeds = models.CharField(max_length=1, choices=Breeds)
    clients = models.ManyToManyField(Clients)

    def __str__(self):
        return self.name


class Employees(models.Model):
    name = models.CharField(max_length=64, verbose_name='Imię')
    surname = models.CharField(max_length=64, verbose_name='Nazwisko')

    def __str__(self):
        return self.name


class Reservation(models.Model):
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    dog = models.ForeignKey(Dogs, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


class Service(models.Model):
    services = models.CharField(max_length=1, choices=Services)
    dog = models.ForeignKey(Dogs, on_delete=models.CASCADE)

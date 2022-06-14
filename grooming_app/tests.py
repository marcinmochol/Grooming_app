from django.test import TestCase
from grooming_app.models import Clients, Dogs, Employees, MyReservation, Service
from django.contrib.auth.models import User

class ModelsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester",
                                             password="qwerty")
        self.clients = Clients.objects.create(name="name",
                                              surname="surname",
                                              e_mail="e_mail",
                                              phone_number="phone_number")
        self.dogs = Dogs.objects.create(dog_name="dog_name",
                                        breed="breed",
                                        age="age",
                                        comment="comment",
                                        clients=self.clients)
        self.employees = Employees.objects.create(name="name",
                                                  surname="surname",
                                                  e_mail="e_mail",
                                                  description="description",
                                                  dog=self.dogs)
        self.service = Service.objects.create(service_name="service_name",
                                              price="price")

        self.myreservation = MyReservation.objects.create(service=self.service,
                                                          dog=self.dogs,
                                                          start_day="2020-01-11",
                                                          start_hour="11:11",
                                                          description="description")

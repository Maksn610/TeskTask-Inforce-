from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        app_label = 'app2'

    def __str__(self):
        return self.name

class Menu(models.Model):
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    date = models.DateField()
    votes = models.IntegerField(default=0)

    class Meta:
        ordering = ['-date', '-votes']

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)

from django.db import models

# Create your models here.

class Property(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

class Unit(models.Model):
    Unit_TYPE = [
        ("1BHK",'1BHK'),
        ("2BHK",'2BHK'),
        ("3BHK",'3BHK'),
        ("4BHK",'4BHK'),
    ]
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    rent_cost = models.DecimalField(max_digits=10, decimal_places=2)
    unit_type = models.CharField(max_length=4, choices=Unit_TYPE)

class Tenant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
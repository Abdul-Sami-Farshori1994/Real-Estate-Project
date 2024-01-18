from django.db import models

# Create your models here.
from property_management.models import Unit

class Tenant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    agreement_end_date = models.DateField()
    monthly_rent_date = models.IntegerField()

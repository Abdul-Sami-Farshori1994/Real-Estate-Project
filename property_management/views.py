from django.shortcuts import render

# Create your views here.
from .models import Property, Unit

def property_list(request):
    properties = Property.objects.all()
    return render(request, 'property_management/property_list.html', {'properties': properties})

def property_detail(request, property_id):
    property = Property.objects.get(id=property_id)
    units = Unit.objects.filter(property=property)
    return render(request, 'property_management/property_detail.html', {'property': property, 'units': units})
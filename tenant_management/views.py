from django.shortcuts import render

# Create your views here.
from .models import Tenant

def tenant_list(request):
    tenants = Tenant.objects.all()
    return render(request, 'tenant_management/tenant_list.html', {'tenants': tenants})

def tenant_detail(request, tenant_id):
    tenant = Tenant.objects.get(id=tenant_id)
    return render(request, 'tenant_management/tenant_detail.html', {'tenant': tenant})

from django.urls import path
from .views import tenant_list, tenant_detail

urlpatterns = [
    path('list/', tenant_list, name='tenant_list'),
    path('<int:tenant_id>/', tenant_detail, name='tenant_detail'),
]
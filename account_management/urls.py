from django.urls import path
from .views import login_view

urlpatterns = [
    path('admin/login/', login_view, name='login'),
]
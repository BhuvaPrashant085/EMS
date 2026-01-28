from django.urls import path
from .views import (
    citizen_dashboard,
    admin_dashboard,
    service_dashboard,
    hospital_dashboard
)

urlpatterns = [
    path('citizen/', citizen_dashboard, name='citizen_dashboard'),
    path('admin/', admin_dashboard, name='admin_dashboard'),
    path('service/', service_dashboard, name='service_dashboard'),
    path('hospital/', hospital_dashboard, name='hospital_dashboard'),
]

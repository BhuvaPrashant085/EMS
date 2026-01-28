from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def citizen_dashboard(request):
    return render(request, 'dashboard/citizen_dashboard.html')

@login_required
def admin_dashboard(request):
    return render(request, 'dashboard/admin_dashboard.html')

@login_required
def service_dashboard(request):
    return render(request, 'dashboard/service_dashboard.html')

@login_required
def hospital_dashboard(request):
    return render(request, 'dashboard/hospital_dashboard.html')

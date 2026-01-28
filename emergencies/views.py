from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Emergency

@login_required
def sos_request(request):
    if request.method == 'POST':
        emergency_type = request.POST['emergency_type']
        lat = request.POST['latitude']
        lng = request.POST['longitude']

        Emergency.objects.create(
            user=request.user,
            emergency_type=emergency_type,
            latitude=lat,
            longitude=lng
        )

        return redirect('citizen_dashboard')

    return render(request, 'emergencies/sos.html')

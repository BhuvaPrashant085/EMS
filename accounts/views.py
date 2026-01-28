from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def role_redirect(request):
    user = request.user

    if user.role == 'CITIZEN':
        return redirect('citizen_dashboard')
    elif user.role in ['OPERATOR', 'ADMIN']:
        return redirect('admin_dashboard')
    elif user.role in ['AMBULANCE', 'POLICE', 'FIRE']:
        return redirect('service_dashboard')
    elif user.role == 'HOSPITAL':
        return redirect('hospital_dashboard')

    return redirect('login')
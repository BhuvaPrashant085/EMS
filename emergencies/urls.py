from django.urls import path
from . import views

urlpatterns = [
    path('sos/', views.sos_request, name='sos'),
]

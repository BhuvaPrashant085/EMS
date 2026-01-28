from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Emergency(models.Model):

    EMERGENCY_TYPE = (
        ('MEDICAL', 'Medical Emergency'),
        ('ACCIDENT', 'Road Accident'),
        ('FIRE', 'Fire Emergency'),
        ('CRIME', 'Crime Emergency'),
        ('DISASTER', 'Natural Disaster'),
    )

    STATUS = (
        ('PENDING', 'Pending'),
        ('ASSIGNED', 'Assigned'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    emergency_type = models.CharField(max_length=20, choices=EMERGENCY_TYPE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    status = models.CharField(max_length=20, choices=STATUS, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.emergency_type} - {self.status}"

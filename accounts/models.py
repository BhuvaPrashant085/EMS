from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    ROLE_CHOICES = (
        ('CITIZEN', 'Citizen'),
        ('OPERATOR', 'Emergency Operator'),
        ('AMBULANCE', 'Ambulance Driver'),
        ('POLICE', 'Police'),
        ('FIRE', 'Fire Fighter'),
        ('HOSPITAL', 'Hospital Staff'),
        ('ADMIN', 'Admin'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='CITIZEN')
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.username} - {self.role}"

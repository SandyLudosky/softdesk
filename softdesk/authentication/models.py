from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    """
    Custom User Model
    """
    age = models.PositiveIntegerField()
    can_be_shared = models.BooleanField(default=False)
    can_be_contacted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

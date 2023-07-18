from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contributor(models.Model):
    """
    Contributor model
    """
    CHOICES = (
        ('A', 'Author'),
        ('C', 'Contributor'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=200, choices=CHOICES)

    def __str__(self):
        return str(self.user)
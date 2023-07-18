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


class Project(models.Model):
    """
    Project Model
    """
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    contributors = models.ManyToManyField(Contributor, blank=True, related_name='projects', default=[])
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=300, blank=True, default='')

    def __str__(self):
        return self.title



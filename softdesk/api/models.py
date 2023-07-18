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
    TYPES_CHOICES = (
        ('B', 'BACKEND'),
        ('F', 'FRONTEND'),
        ('I', 'IOS'),
        ('A', 'Android'),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    contributors = models.ManyToManyField(Contributor, blank=True, related_name='projects', default=[])
    project_type = models.CharField(max_length=9, choices=TYPES_CHOICES, default='')
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=300, blank=True, default='')

    def __str__(self):
        return self.title


class Issue(models.Model):
    """
    Issue Model
    """
    TAG_CHOICES = (
        ('B', 'Bug'),
        ('T', 'TASK'),
        ('F', 'FEATURE'),
    )
    STATUS_CHOICES = (
        ('T', 'TODO'),
        ('I', 'IN PROGRESS'),
        ('F', 'FINISHED')
    )
    PRIORITY_CHOICES = (
        ('L', 'LOW'),
        ('M', 'MEDIUM'),
        ('H', 'HIGH'),
    )

    created_at = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, related_name='issues', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=300)
    tag = models.CharField(max_length=50, choices=TAG_CHOICES)
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    assigned_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='assigned_user',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title

class Comment(models.Model):
    """
    Comment model
    """
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    issue = models.ForeignKey(Issue, related_name='comments', on_delete=models.CASCADE)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.description
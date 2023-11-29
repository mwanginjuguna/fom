from django.db import models
from django.utils import timezone

# Create your models here.
class CommonMeta(models.Model):
    title = models.CharField("Name/title", max_length=400)
    description = models.TextField('Meta description')
    created_at = models.DateTimeField("Date and time of creation", auto_now_add=True)
    updated_at = models.DateTimeField("Date and time of last update.", auto_now=True)


    def __str__(self):
        return self.title

    class Meta():
        abstract = True


class Project(models.Model):
    STATUS_CHOICES = (
        ('planning', 'Planning'),
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('on_hold', 'On Hold'),
        ('canceled', 'Canceled'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planning')
    team_members = models.ManyToManyField(User, related_name='project_team_members')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_projects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Additional Fields
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    client = models.CharField(max_length=255, null=True, blank=True)
    priority = models.PositiveIntegerField(default=1)
    tags = models.ManyToManyField('Tag', related_name='project_tags', blank=True)
    # Add more fields as needed

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Objective(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField()
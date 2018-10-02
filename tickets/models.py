from django.db import models
from django.utils import timezone

# Create your models here.
class Ticket(models.Model):
    """A single ticket release"""
    ISSUE_TYPE_CHOICES = (
        ('B', 'Bug'),
        ('F', 'Feature')
        )
    issue_type = models.CharField(
        max_length=7,
        choices=ISSUE_TYPE_CHOICES,
        default="Bug",
    )
    issue_name = models.CharField(max_length=254, default='')
    issue_detail = models.TextField()
    STATUS_CHOICES = (
        ('TD', 'ToDo'),
        ('DG', 'Doing'),
        ('DN', 'Done')
        )
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default="ToDo",
    )
    due_date = models.DateField(default=timezone.now)
    urgent = models.BooleanField()
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to='img', blank=True, null=True)
    tag = models.CharField(max_length=30, blank=True, null=True)
    
    def __unicode__(self):
        return self.issue_type
    
from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Labels(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    label_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL', db_index=True)


class Tasks(models.Model):
    NOT_STARTED = 'Not started'
    IN_PROGRESS = 'In progress'
    COMPLETE = 'Complete'

    STATE_CHOICES = [
        (NOT_STARTED, 'Not started'),
        (IN_PROGRESS, 'In progress'),
        (COMPLETE, 'Complete'),
    ]

    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL', db_index=True)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default=NOT_STARTED)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True)
    labels = models.ManyToManyField(Labels)



from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class State(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL', db_index=True)


class Task(models.Model):
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL', db_index=True)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    state = models.ForeignKey('State', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True)


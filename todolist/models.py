from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
    )
    date = models.DateField()
    title = models.CharField(max_length=200)
    description = models.TextField()
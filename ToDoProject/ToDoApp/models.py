from django.db import models
from django.contrib.auth.models import User

class ToDoItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=200)
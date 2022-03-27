from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.last_name} | {self.first_name} '


class Biography(models.Model):
    text = models.TextField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Brend(models.Model):
    name = models.CharField(max_length=64)
    users = models.ManyToManyField(User)

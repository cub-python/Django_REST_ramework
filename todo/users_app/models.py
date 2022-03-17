from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # first_name = models.CharField(max_length=64)
    # last_name = models.CharField(max_length=64)
    # # birthday_year = models.PositiveBigIntegerField()
    email = models.EmailField(unique=True)


class Biography(models.Model):
    text = models.TextField(null=True, blank=True)
    author = models.OneToOneField(User, on_delete=models.CASCADE)


class Brend(models.Model):
    name = models.CharField(max_length=64)
    users = models.ManyToManyField(User)

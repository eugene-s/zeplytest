from django.db import models
from django_cryptography.fields import encrypt


class Wallet(models.Model):
    seed = encrypt(models.TextField())
    sequence = encrypt(models.IntegerField())
    public_key = models.TextField()
    private_key = encrypt(models.TextField())

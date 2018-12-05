from django.db import models

from authentication.models import User


class Cup(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    barcode = models.CharField(max_length=50, unique=True)

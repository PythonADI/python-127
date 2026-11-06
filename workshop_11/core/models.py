from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=60)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField()
    production_date = models.DateField()
    expiry_date = models.DateField()

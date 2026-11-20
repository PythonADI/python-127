from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.utils.text import slugify

class Product(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=60, unique=True, blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField()
    production_date = models.DateField()
    expiry_date = models.DateField()
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower("name"),
                name="unique_lower_name",
                violation_error_message="Name must be unique"
            )
        ]

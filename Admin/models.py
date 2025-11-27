from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    brand = models.CharField(max_length=15, default="Unknown")
    category = models.CharField(max_length=15, default="General")
    quantity = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name
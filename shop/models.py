from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('WOMEN', 'Womens'),
        ('MEN', 'Mens'),
        ('KIDS', 'Kids'),
    ]
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    offer = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


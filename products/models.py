from django.db import models

class Product(models.Model):
    sku = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=254)
    roast = models.CharField(max_length=254)
    location = models.CharField(max_length=254)
    origin = models.CharField(max_length=254)
    bag_100g_USD = models.DecimalField(max_digits=3, decimal_places=2)
    rating = models.IntegerField(null=True, blank=True)
    review = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
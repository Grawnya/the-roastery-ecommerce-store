from django.db import models

roast_choices = (
    (1, 'Light'),
    (2, 'Medium-Light'),
    (3, 'Medium'),
    (4, 'Medium-Dark'),
    (5, 'Dark'),
    )

class Product(models.Model):
    sku = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=254)
    roast = models.CharField(max_length=254, null=False, choices=roast_choices)
    location = models.CharField(max_length=254)
    origin = models.CharField(max_length=254)
    bag_100g_USD = models.DecimalField(max_digits=4, decimal_places=2)
    rating = models.IntegerField(null=True, blank=True)
    review = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
from django.db import models

roast_choices = (
    ('Light', 'Light'),
    ('Medium-Light', 'Medium-Light'),
    ('Medium', 'Medium'),
    ('Medium-Dark', 'Medium-Dark'),
    ('Dark', 'Dark'),
    )

location_choices = (
    ('Africa', 'Africa'),
    ('South America', 'South America'),
    ('Central America', 'Central America'),
    ('North America', 'North America'),
    ('Asia', 'Asia'),
    ('Europe', 'Europe'),
    ('Oceania', 'Oceania'),
)


class Product(models.Model):
    """Product model of all products."""

    sku = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=254)
    roast = models.CharField(max_length=254, null=False,
                             choices=roast_choices)
    location = models.CharField(max_length=254, choices=location_choices)
    origin = models.CharField(max_length=254)
    bag_100g_USD = models.DecimalField(max_digits=4, decimal_places=2)
    rating = models.IntegerField(null=True, blank=True)
    review = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        """Representation of Product class."""
        return self.name

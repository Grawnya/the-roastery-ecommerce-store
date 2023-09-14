from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

roast_choices = (
    ('light', 'Light'),
    ('medium_light', 'Medium-Light'),
    ('medium', 'Medium'),
    ('medium_dark', 'Medium Dark'),
    ('dark', 'Dark'),
    )

coffee_choices = (
    ('hawaii', 'Hawaii'),
    ('brazil', 'Brazil'),
    ('ethiopia', 'Ethiopia'),
    ('panama', 'Panama'),
    ('indonesia', 'Indonesia'),
    ('peru', 'Peru'),
    ('costa_rica', 'Costa Rica'),
    ('burundi', 'Burundi'),
    ('colombia', 'Colombia'),
    ('taiwan', 'Taiwan'),
    ('mexico', 'Mexico'),
    ('nepal', 'Nepal'),
    ('kenya', 'Kenya'),
    )


class Favourites(models.Model):
    """User's Favourites model."""

    website_user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField()
    coffee_type = models.CharField(max_length=50, choices=coffee_choices,
                                   default='colombia', null=True, blank=True)
    roast = models.CharField(max_length=30, choices=roast_choices,
                             default='light', null=True, blank=True)

    def __str__(self):
        """Representation of Favourites Model."""
        return f'I love {self.roast} roasted coffee from {self.coffee_type}!'


class WebsiteUser(models.Model):
    """WebsiteUser's details."""

    website_user = models.OneToOneField(User, on_delete=models.CASCADE,
                                        related_name='userprofile')
    profile_full_name = models.CharField(max_length=50, null=False,
                                         blank=False)
    profile_email = models.EmailField(max_length=254, null=False, blank=False)
    profile_phone_number = models.CharField(max_length=30,
                                            null=True, blank=True)
    profile_street_address1 = models.CharField(max_length=100,
                                               null=True, blank=True)
    profile_street_address2 = models.CharField(max_length=100,
                                               null=True, blank=True)
    profile_town_or_city = models.CharField(max_length=50,
                                            null=True, blank=True)
    profile_county = models.CharField(max_length=90,
                                      null=True, blank=True)
    profile_postcode = models.CharField(max_length=20,
                                        null=True, blank=True)
    profile_country = CountryField(blank_label='Global Citizen',
                                   null=True, blank=True)

    def __str__(self):
        """Representation of WebsiteUser Model."""
        return self.website_user.username


@receiver(post_save, sender=User)
def deal_with_user_profile(sender, instance, created, **kwargs):
    """Dealing with a user profile."""
    if created:
        WebsiteUser.objects.create(website_user=instance)

from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class WebsiteUser(models.Model):
    website_user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_full_name = models.CharField(max_length=50, null=False, blank=False)
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
        return self.website_user.username


@receiver(post_save, sender=User)
def deal_with_user_profile(sender, instance, created, **kwargs):
    if created:
        WebsiteUser.objects.create(user=instance)
    instance.userprofile.save()
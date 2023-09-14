from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import *


@receiver(post_save, sender=OrderItem)
def update_on_save(sender, instance, created, **kwargs):
    """Update item number."""
    instance.order_id.update_total()


@receiver(post_delete, sender=OrderItem)
def update_on_delete(sender, instance, **kwargs):
    """Delete item from bag."""
    instance.order_id.update_total()

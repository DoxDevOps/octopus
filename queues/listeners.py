from django.db.models.signals import post_save
from django.dispatch import receiver
from routes.models import Route
from . import models, transmissions


@receiver(post_save, sender=models.QueueItem)
def queued_item_created(sender, instance, created, **kwargs):
    """runs when an item is created"""

    if created:
        sms = transmissions.TextMessage("0998006237", "This is the message to send.")
        sms.connect_phone()
        sms.send_message()
        sms.disconnect_phone()

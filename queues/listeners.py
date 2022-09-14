from django.db.models.signals import post_save
from django.dispatch import receiver
from routes.models import Route
from . import models, transmissions


@receiver(post_save, sender=models.QueueItem)
def queued_item_created(sender, instance, created, **kwargs):
    """runs when an item is created in the queue"""

    if created:
        # [TODO] Add items to a "real" queue like Celery?
        # [TODO] Check if routes are available. Start checking for the high weighted going down
        # [TODO] If default routes are NOT available default to SMS route
        sms = transmissions.TextMessage("0998006237", "This is the message to send.")
        sms.connect_phone()
        sms.send_message()
        sms.disconnect_phone()

import os
from django.db.models.signals import post_save
from django.dispatch import receiver
from routes.models import Route
from . import models, transmissions
from routes import RouteType
import logging


@receiver(post_save, sender=models.QueueItem)
def queue_item_created(sender, instance, created, **kwargs):
    """runs when an item is created in the queue"""

    if created:
        # [TODO] add items to a "real" queue like Celery?
        # [TODO] check if other routes are available. Start checking for the high weighted going down
        # [TODO] if default routes are NOT available default to SMS route

        routes = Route.objects.all().order_by("weight")

        available_routes = []

        if not os.environ.get("USE_SMS_ROUTE_ONLY", True):

            logging.info("Trying to find available route")

            for route in routes:

                # the assumption is that SMS route is always available, so no need to check that route
                # and haven't figured out how to check it's availability anyways

                if route.type != RouteType.SMS:

                    logging.info("PINGING route %s", route)

                    # [TODO] add ping functionality to check if route is available
                    # [TODO] if route is available add to available_routes list

            # [TODO] check if available_routes is not empty, if not, get available_route[0] and send the data

        else:

            logging.info("Using the %s route", RouteType.SMS)

            sms = transmissions.TextMessage(
                os.environ.get("INBOUND_SMS_SHORT_CODE", "0999111222")
            )
            sms.connect_phone()
            sms.send_message()
            sms.disconnect_phone()

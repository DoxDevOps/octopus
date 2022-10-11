from django.db import transaction
from rest_framework import viewsets

import logging

from . import models, serializers

logger = logging.getLogger(__name__)


class ItemQueueViewSet(viewsets.ModelViewSet):
    """Item queuing"""

    queryset = models.QueueItem.objects.all().order_by("-created_at")
    serializer_class = serializers.ItemQueueSerializer

    def perform_create(self, serializer: serializers.ItemQueueSerializer):

        with transaction.atomic():

            item_queue: models.QueueItem = serializer.save()

            logger.info("Queued item from %s", item_queue.source.get_source_name)

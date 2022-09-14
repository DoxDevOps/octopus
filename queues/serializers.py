from ipaddress import ip_address
from rest_framework import serializers
from . import models, utils
import logging


class ItemQueueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.QueueItem
        fields = [
            "id",
            "destination",
            "payload",
            "encrypt_before_sending",
        ]

    def create(self, validated_data):

        ip_address = self.context.get("request").META.get("REMOTE_ADDR")

        logging.info("Trying to find source for %s", ip_address)

        validated_data["source"] = utils.get_source_from_ip(ip_address)

        return super().create(validated_data)

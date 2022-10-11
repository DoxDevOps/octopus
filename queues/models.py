import os

from django.db import models
from routes.models import BaseModel
from django.core.exceptions import ObjectDoesNotExist


from . import QueueStatus


class Source(BaseModel):
    """Where the data is coming from"""

    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    default_destination = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        try:
            return str(self.name)
        except ObjectDoesNotExist:
            return "Unknown source"

    def __repr__(self) -> str:
        return super().__repr__()

    @property
    def get_source_name(self) -> str:
        "Returns the name of the source."

        return self.name

    @property
    def get_default_destination(self) -> str:
        """Returns the default destination"""

        return self.default_destination

    __repr__ = __str__


class QueueItem(BaseModel):
    """Queued items"""

    source = models.ForeignKey(Source, on_delete=models.SET_NULL, null=True)
    destination = models.CharField(max_length=255, null=True)
    payload = models.TextField(null=True, blank=True)
    encrypt_before_sending = models.BooleanField(default=True, verbose_name="encrypt")
    status = models.CharField(
        choices=QueueStatus.CHOICES,
        max_length=255,
        null=True,
        blank=True,
        default=QueueStatus.QUEUED,
    )
    retry_attempt_count = models.IntegerField(default=0)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        try:
            return f"Item from {self.source.name}"
        except ObjectDoesNotExist:
            return "Unknown queue item"

    @property
    def get_allowed_retries(self):
        """Get how many times we should try to send the data to the destination"""

        if self.source.default_retry_allowed > self.retry_allowed:
            return self.source.default_retry_count_allowed

        return self.retry_allowed

    @property
    def get_payload(self):
        return self.payload

    def encrypt(self):
        from cryptography.fernet import Fernet

        key = os.environ.get("ENCRYPTION_KEY", "SOME-VERY-COMPLICATED-ENCYPTION-KEY")
        fernet = Fernet(key)
        return fernet.encrypt(self.payload.encode())

    __repr__ = __str__

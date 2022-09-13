from django.utils.translation import pgettext_lazy


class QueueStatus:
    """Flags for queue status"""

    QUEUED = "Queued"
    SENT = "Sent"
    FAILED = "Failed"

    CHOICES = [
        (QUEUED, pgettext_lazy("queue status", "Queued")),
        (SENT, pgettext_lazy("queue status", "Sent")),
        (FAILED, pgettext_lazy("queue status", "Failed")),
    ]

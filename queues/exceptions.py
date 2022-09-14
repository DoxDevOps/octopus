"""All exceptions for Queues"""


class QueueError(Exception):
    """Base class for all errors"""


class SourceNotFound(QueueError):
    """Flags missing payload source"""

import logging
from typing import Any
from . import models, exceptions


def get_source_from_ip(ip_address: str) -> Any:
    """Gets the source from ip_address"""

    logging.debug("Retrieving source from IP address, %s", ip_address)

    try:
        source_obj = models.Source.objects.get(address=ip_address)

    except models.Source.DoesNotExist:
        raise exceptions.SourceNotFound(
            f"No source found matching IP address, {ip_address}"
        )

    return source_obj

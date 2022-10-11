import uuid
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from . import RouteStatus, RouteType


class UuidField(models.CharField):
    """A version 4 UUID field"""

    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 128
        kwargs["default"] = uuid.uuid4

        if "unique" not in kwargs:
            kwargs["unique"] = True
        if "null" not in kwargs:
            kwargs["null"] = False

        super(type(self), self).__init__(*args, **kwargs)


class BaseModel(models.Model):
    """Adds a number of fields common to most models within this App"""

    class Meta:
        abstract = True

    uuid = UuidField()
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True)


class Route(BaseModel):
    """Connectivity route between two sites"""

    name = models.CharField(
        max_length=255, null=True, help_text="The name of the route between two nodes"
    )
    description = models.TextField(
        null=True,
        blank=True,
        help_text="Describe your route. For example SMS route or EGPAF WAN route",
    )
    type = models.CharField(choices=RouteType.CHOICES, max_length=255, null=True)
    weight = models.IntegerField(
        default=1,
        unique=True,
        help_text="A route should have a unique weighting. No two routes can have same weighting.",
    )
    status = models.CharField(
        choices=RouteStatus.CHOICES,
        max_length=255,
        null=True,
        blank=True,
        default=RouteStatus.UNKNOWN,
    )
    address = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="This can be a default gateway or anything similar that can ascertain if a route is UP.",
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        try:
            return str(self.name)
        except ObjectDoesNotExist:
            return "Unknown route"

    def __repr__(self) -> str:
        return super().__repr__()

    @property
    def get_route_name(self) -> str:
        "Returns the name of the route."

        return self.name

    @property
    def get_route_address(self) -> str:
        """Returns the address of the route"""

        return self.address

    @property
    def is_route_available(self) -> bool:
        """
        Checks if route status is UP

        [TODO] The idea is to have a separate service checking the availability of the route and updating this field
        However, for now we simply ping the gateway of the route to check if its available
        """

        if self.status != RouteStatus.UP:
            return False

        return True

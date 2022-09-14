from django.utils.translation import pgettext_lazy


class RouteStatus:
    """Flags for route reachability"""

    UP = "Up"
    DOWN = "Down"
    UNKNOWN = "Unknown"

    CHOICES = [
        (UP, pgettext_lazy("route status", "Up")),
        (DOWN, pgettext_lazy("route status", "Down")),
        (UNKNOWN, pgettext_lazy("route status", "Unknown")),
    ]

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


class RouteType:
    """Types of routes"""

    INTERNET = "Internet"
    VPN = "VPN"
    SMS = "SMS"

    CHOICES = [
        (INTERNET, pgettext_lazy("route type", "Internet")),
        (VPN, pgettext_lazy("route type", "VPN")),
        (SMS, pgettext_lazy("route type", "SMS")),
    ]

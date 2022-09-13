from django.contrib import admin
from . import models


@admin.register(models.Route)
class RouteAdmin(admin.ModelAdmin):
    pass

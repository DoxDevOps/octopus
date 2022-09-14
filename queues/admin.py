from django.contrib import admin
from . import models


@admin.register(models.Source)
class RouteAdmin(admin.ModelAdmin):
    pass


@admin.register(models.QueueItem)
class RouteAdmin(admin.ModelAdmin):
    pass

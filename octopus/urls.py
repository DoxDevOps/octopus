from django.contrib import admin
from django.urls import include, path

import queues.urls as queue_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(queue_urls.urlpatterns)),
]

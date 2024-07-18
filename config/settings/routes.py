from django.contrib import admin
from django.urls import include, path

from config.env import ENV

urlpatterns = [
    path("", include("apps.pages.urls")),
    path(f"{ENV.get("ADMIN_PATH", 'admin/')}/", admin.site.urls),
]

from django.contrib import admin
from django.urls import path, include
from config.env import ENV

urlpatterns = [
    path("", include("apps.pages.urls")),
    path(f"{ENV.get("ADMIN_PATH", 'admin/')}/", admin.site.urls),
]

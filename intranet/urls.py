from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # Built-in auth views: login/ logout/ password_change/ password_reset/ ...
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("portal.urls")),
]

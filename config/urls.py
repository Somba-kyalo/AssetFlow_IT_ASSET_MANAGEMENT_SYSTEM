from django.contrib import admin
from django.urls import include, path

handler404 = "dashboard.views.error_404"
handler500 = "dashboard.views.error_500"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("dashboard.urls")),
    path("", include("registration.urls")),
]
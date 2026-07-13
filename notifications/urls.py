from django.urls import path
from . import views

urlpatterns = [

    path("", views.notifications, name="notifications"),

    path("notification-detail/<int:id>/", views.notification_detail, name="notification_detail"),

    path("maintenance-alerts/", views.maintenance_alerts, name="maintenance_alerts"),

    path("assignment-alerts/", views.assignment_alerts, name="assignment_alerts"),

    path("warranty-alerts/", views.warranty_alerts, name="warranty_alerts"),

]
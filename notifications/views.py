from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def notifications(request):
    return render(request, "notifications/notifications.html")


def notification_detail(request, id):
    return render(request, "notifications/notification_detail.html")


def maintenance_alerts(request):
    return render(request, "notifications/maintenance_alerts.html")


def assignment_alerts(request):
    return render(request, "notifications/assignment_alerts.html")


def warranty_alerts(request):
    return render(request, "notifications/warranty_alerts.html")
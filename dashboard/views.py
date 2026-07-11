from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def home(request):
    return render(request, "home.html")


def dashboard(request):
    return render(request, "dashboard/dashboard.html")


def analytics(request):
    return render(request, "dashboard/analytics.html")


def recent_activity(request):
    return render(request, "dashboard/recent_activity.html")


def statistics(request):
    return render(request, "dashboard/statistics.html")


def error_404(request, exception):
    return render(request, "404.html", status=404)


def error_500(request):
    return render(request, "500.html", status=500)
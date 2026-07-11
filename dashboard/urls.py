from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboard/analytics/", views.analytics, name="analytics"),
    path("dashboard/recent-activity/", views.recent_activity, name="recent_activity"),
    path("dashboard/statistics/", views.statistics, name="statistics"),
]
from django.urls import path
from . import views

urlpatterns = [

    path("maintenance/", views.maintenance, name="maintenance"),

    path("maintenance-detail/<int:id>/", views.maintenance_detail, name="maintenance_detail"),

    path("report-issue/", views.report_issue, name="report_issue"),

    path("add-maintenance/", views.add_maintenance, name="add_maintenance"),

    path("edit-maintenance/<int:id>/", views.edit_maintenance, name="edit_maintenance"),

    path("maintenance-history/", views.maintenance_history, name="maintenance_history"),

    path("pending-repairs/", views.pending_repairs, name="pending_repairs"),

    path("completed-repairs/", views.completed_repairs, name="completed_repairs"),

    path("maintenance-schedule/", views.maintenance_schedule, name="maintenance_schedule"),

]
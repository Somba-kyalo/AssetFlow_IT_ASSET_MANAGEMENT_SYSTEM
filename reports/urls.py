from django.urls import path
from . import views

urlpatterns = [

    path("", views.reports, name="reports"),

    path("asset_report/", views.asset_report, name="asset_report"),

    path("department_report/", views.department_report, name="department_report"),

    path("employee_report/", views.employee_report, name="employee_report"),

    path("maintenance_report/", views.maintenance_report, name="maintenance_report"),

    path("supplier_report/", views.supplier_report, name="supplier_report"),

    path("warranty_report/", views.warranty_report, name="warranty_report"),

    path("export_pdf/", views.export_pdf, name="export_pdf"),

    path("export_excel/", views.export_excel, name="export_excel"),

]
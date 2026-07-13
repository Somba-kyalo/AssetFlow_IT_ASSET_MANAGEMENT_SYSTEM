from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def reports(request):
    return render(request, "reports/reports.html")


def asset_report(request):
    return render(request, "reports/asset_report.html")


def department_report(request):
    return render(request, "reports/department_report.html")


def employee_report(request):
    return render(request, "reports/employee_report.html")


def maintenance_report(request):
    return render(request, "reports/maintenance_report.html")


def supplier_report(request):
    return render(request, "reports/supplier_report.html")


def warranty_report(request):
    return render(request, "reports/warranty_report.html")


def export_pdf(request):
    return render(request, "reports/export_pdf.html")


def export_excel(request):
    return render(request, "reports/export_excel.html")
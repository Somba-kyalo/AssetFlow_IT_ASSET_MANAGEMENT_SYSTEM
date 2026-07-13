from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def maintenance(request):
    return render(request, "maintenance/maintenance.html")

def maintenance_detail(request, id):
    return render(request, "maintenance/maintenance_detail.html")

def report_issue(request):
    return render(request, "maintenance/report_issue.html")

def add_maintenance(request):
    return render(request, "maintenance/add_maintenance.html")

def edit_maintenance(request, id):
    return render(request, "maintenance/edit_maintenance.html")

def maintenance_history(request):
    return render(request, "maintenance/maintenance_history.html")

def pending_repairs(request):
    return render(request, "maintenance/pending_repairs.html")

def completed_repairs(request):
    return render(request, "maintenance/completed_repairs.html")

def maintenance_schedule(request):
    return render(request, "maintenance/maintenance_schedule.html")
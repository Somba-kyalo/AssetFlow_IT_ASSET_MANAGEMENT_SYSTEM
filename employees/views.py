from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def employees(request):
    return render(request, "employees/employees.html")

def employee_detail(request, id):
    return render(request, "employees/employee_detail.html")

def add_employee(request):
    return render(request, "employees/add_employee.html")

def edit_employee(request, id):
    return render(request, "employees/edit_employee.html")

def delete_employee(request, id):
    return render(request, "employees/delete_employee.html")

def employee_assets(request, id):
    return render(request, "employees/employee_assets.html")

def employee_profile(request, id):
    return render(request, "employees/employee_profile.html")
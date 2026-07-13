from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def departments(request):
    return render(request, "departments/departments.html")

def department_detail(request, id):
    return render(request, "departments/department_detail.html")

def add_department(request):
    return render(request, "departments/add_department.html")

def edit_department(request, id):
    return render(request, "departments/edit_department.html")

def delete_department(request, id):
    return render(request, "departments/delete_department.html")

def department_assets(request, id):
    return render(request, "departments/department_assets.html")